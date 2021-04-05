from meps_db.processors.encoders.population_characteristics_encoder import PopulationCharacteristicsEncoder
from meps_db.processors.encoders.office_based_visits_encoder import OfficeBasedVisitsEncoder
from meps_db.utilities.universal_utilities import UniversalUtilityFunctions as uuf

class OfficeBasedUtilization:
    """ Analysis class for downstream research. Processes data from the PopulationCharacteristics table and office
    based event tables to generate metrics associated with utilization. """

    def __init__(self, years):
        """ 
        Required Inputs:
            years: years to analyze
        """

        self.years = years
        self.all_population_characteristics = {}
        self.all_office_based_events = {}

        self.max_year = max(self.years)
        for year in self.years:
            self.all_population_characteristics[year] = PopulationCharacteristicsEncoder(year=year).run()
            self.all_office_based_events[year] = OfficeBasedVisitsEncoder(year=year).run()

    
    def calculate_office_based_metrics(self):
        """ Calculates utilization based metrics related to office vists. 

        For the following groups:
            - age 0-18
            - age 18-65
            - age 65+
            - Has Usual Source of Care
            - Does not have Usual Source of Care
        
        Captures the following metrics:
            - % of population with at least one office based event
            - % of the population with at least one primary care event
            - mean office based visits
            - median office based visits
            - mean primary care visits
            - median primary care visits
            - sample_size, total respondents within group
            - sample_population_size, total weight of respondents within group

        """

        annual_data = []
        for year in self.years:
            office_based_tracker = []
            for resp, resp_dict in self.all_population_characteristics[year].items():
                
                office_based_visit_count = (
                    len(self.all_office_based_events[year][resp]) if resp in self.all_office_based_events[year] else 0
                )
                primary_care_visit_count = (
                    len([ob for ob in self.all_office_based_events[year][resp] if ob["primary_care_event"]]) 
                    if resp in self.all_office_based_events[year] else 0
                )

                office_based_tracker.append(
                    {   
                        "id": resp,
                        "age": resp_dict["characteristics"]["age"],
                        "have_usc": resp_dict["characteristics"]["have_usc"],
                        "weight": resp_dict["characteristics"]["weight"],
                        "office_based_visit_count": office_based_visit_count,
                        "primary_care_visit_count": primary_care_visit_count
                    }
                )

            annual_data.extend(self.generate_metrics(office_based_tracker=office_based_tracker, year=year))

        return annual_data
    
    @staticmethod
    def generate_metrics(office_based_tracker, year):
        """ Takes a list of respondent characteristic and utilization dictionaries. Splits into groups and summarizes
        data. Return a list of dictionaries. """

        all_cat_metrics = []
        total_valid_population_weight = sum(
            [resp["weight"] for resp in office_based_tracker if resp["have_usc"] in {"YES", "NO"}]
        )
        for age_cat, min_age, max_age in [
            ("All Ages", 0, 999), ("Under 18", 0,18), ("18-65", 18,65), ("Over 65", 65, 999)
        ]:
            for usc_cat, usc_status in [("Any USC Status", "ANY"), ("Has USC", "YES"),("No USC", "NO")]:
                
                if usc_status == "ANY":
                    focus_group = [
                        resp_history for resp_history in office_based_tracker
                        if min_age <= resp_history["age"] < max_age
                    ]
                else:
                    focus_group = [
                        resp_history for resp_history in office_based_tracker
                        if min_age <= resp_history["age"] < max_age
                        and resp_history["have_usc"] == usc_status
                    ]
   
                focus_pop_weight = sum([resp["weight"] for resp in focus_group])
                at_least_one_ob = sum([resp["weight"] for resp in focus_group if resp["office_based_visit_count"] > 0])
                at_least_one_pcp = sum(
                    [resp["weight"] for resp in focus_group if resp["primary_care_visit_count"] > 0]
                )

                ob_values = [resp["office_based_visit_count"] for resp in focus_group]
                pcp_values = [resp["primary_care_visit_count"] for resp in focus_group]
                weights = [resp["weight"] for resp in focus_group]

                metrics = {
                    "year": year,
                    "age_group": age_cat,
                    "usc_cat": usc_cat,
                    "at_least_one_ob_visits": at_least_one_ob/focus_pop_weight,
                    "at_least_one_pcp_visits": at_least_one_pcp/focus_pop_weight,
                    "mean_ob_visits": uuf.weighted_average(values_list=ob_values, weights=weights),
                    "median_ob_visits": uuf.weighted_median(values_list=ob_values, weights=weights),
                    "mean_pcp_visits": uuf.weighted_average(values_list=pcp_values, weights=weights),
                    "median_pcp_visits": uuf.weighted_median(values_list=pcp_values, weights=weights),
                    "sample_size": len(focus_group),
                    "sample_population_size": focus_pop_weight,
                    "total_valid_population_weight": total_valid_population_weight,
                }

                all_cat_metrics.append(metrics)
        
        return all_cat_metrics
