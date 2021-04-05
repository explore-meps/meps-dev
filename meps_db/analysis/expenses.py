import cpi

from meps_db.processors.encoders.population_characteristics_encoder import PopulationCharacteristicsEncoder
from meps_db.utilities.universal_utilities import UniversalUtilityFunctions as uuf

class ExpensesAnalyzer:
    """ Analysis class for downstream research. Processes data from the PopulationCharacteristics table and event
    tables to generated metrics associated with expenses. All expense values are adjusted to the most recent year
    provided in the years input. """

    def __init__(self, years):
        """ 
        Required Inputs:
            years: years to analyze
        """

        self.years = years
        self.all_population_characteristics = {}

        self.max_year = max(self.years)
        for year in self.years:
            self.all_population_characteristics[year] = PopulationCharacteristicsEncoder(year=year).run()

        self.SERVICES_EXPENDITURES = [
            ("Any Services", ["total_expenditures"]),
            ("Hospital Inpatient", ["hospital_inpatient_expenditures"]),
            ("Ambulatory", ["office_based_expenditures", "outpatient_expenditures", "emergency_room_expenditures"]),
            ("Prescribed Medicines", ["prescription_medicine_expenditures"]),
            ("Dental Services", ["dental_expenditures"]),
            (
                "Home Health Care and Other Medical Services and Equipment",
                [
                    "home_health_agency_expenditures",
                    "home_health_nonagency_expenditures",
                    "other_medical_expenditures",
                    "vision_expenditures",
                ],
            ),
        ]

    def calculate_any_expenses(self):
        """ Stratifies the population by age groups: Over 65 and Under 65. For each year and age group calculates the
        percent of the age group with ANY health care expenses from various sources. Return as a list of dictionaries
        """

        any_expense = []

        for year, population_characteristics in self.all_population_characteristics.items():
            for service_name, fields in self.SERVICES_EXPENDITURES:

                service_exp, service_exp_under_65, service_exp_over_65 = [], [], []
                service_exp_weight, service_exp_under_65_weight, service_exp_over_65_weight = [], [], []

                for resp_dict in population_characteristics.values():
                    rp = resp_dict["characteristics"]
                    resp_service_exp = sum([rp[field] for field in fields]) > 0

                    service_exp.append(resp_service_exp)
                    service_exp_weight.append(rp["weight"])

                    if rp["age"] < 65:
                        service_exp_under_65.append(resp_service_exp)
                        service_exp_under_65_weight.append(rp["weight"])

                    if rp["age"] >= 65:
                        service_exp_over_65.append(resp_service_exp)
                        service_exp_over_65_weight.append(rp["weight"])

                for age_group, values, weights in [
                    ("All Ages", service_exp, service_exp_weight),
                    ("Under 65", service_exp_under_65, service_exp_under_65_weight),
                    ("Over 65", service_exp_over_65, service_exp_over_65_weight),
                ]:

                    any_expense.append(
                        {
                            "year": year,
                            "services": service_name,
                            "age_group": age_group,
                            "pct_with_expenses": uuf.weighted_pct(bool_list=values, weights=weights),
                        }
                    )
        return any_expense

    def calculate_expenses_metrics(self):
        """ Stratifies the population by age groups: Over 65 and Under 65. For each year and age group calculates the
        mean and median health care expenses for each the age group from various sources. Only calculates these
        values for respondents with any expenses in that service. Return as a list of dictionaries.
        """

        expenses = []

        for year, population_characteristics in self.all_population_characteristics.items():
            for service_name, fields in self.SERVICES_EXPENDITURES:
                service_exp, service_exp_under_65, service_exp_over_65 = [], [], []
                service_exp_weight, service_exp_under_65_weight, service_exp_over_65_weight = [], [], []

                for resp_dict in population_characteristics.values():
                    rp = resp_dict["characteristics"]
                    resp_service_exp = sum([rp[field] for field in fields])

                    if resp_service_exp > 0:

                        service_exp.append(resp_service_exp)
                        service_exp_weight.append(rp["weight"])

                        if rp["age"] < 65:
                            service_exp_under_65.append(resp_service_exp)
                            service_exp_under_65_weight.append(rp["weight"])

                        if rp["age"] >= 65:
                            service_exp_over_65.append(resp_service_exp)
                            service_exp_over_65_weight.append(rp["weight"])

                for age_group, values, weights in [
                    ("All Ages", service_exp, service_exp_weight),
                    ("Under 65", service_exp_under_65, service_exp_under_65_weight),
                    ("Over 65", service_exp_over_65, service_exp_over_65_weight),
                ]:

                    expenses.append(
                        {
                            "year": year,
                            "services": service_name,
                            "age_group": age_group,
                            "mean": cpi.inflate(
                                uuf.weighted_average(values_list=values, weights=weights), year, to=self.max_year
                            ),
                            "median": cpi.inflate(
                                uuf.weighted_median(values_list=values, weights=weights), year, to=self.max_year
                            ),
                        }
                    )

        return expenses

    def calculate_expenses_metrics_by_insurance(self):
        """ Stratifies the population by age groups: Over 65 and Under 65 and insurance type. For each year and age
        group calculates the mean and median health care expenses for each the age group from various sources. Only
        calculates these values for respondents with any expenses in that service. Return as a list of dictionaries.
        """

        expenses_insurance = []

        for year, population_characteristics in self.all_population_characteristics.items():

            exp_under_65, private_exp_under_65 = [], []
            public_exp_under_65, uninsured_under_65 = [], []
            exp_under_65_weight, private_exp_under_65_weight = [], []
            public_exp_under_65_weight, uninsured_under_65_weight = [], []

            exp_over_65, medicare_exp_over_65, = [], []
            medicare_private_exp_over_65, medicare_public_exp_over_65 = [], []
            exp_over_65_weight, medicare_exp_over_65_weight = [], []
            medicare_private_exp_over_65_weight, medicare_public_exp_over_65_weight = [], []

            for resp_dict in population_characteristics.values():
                rp = resp_dict["characteristics"]
                resp_service_exp = rp["total_expenditures"]

                if resp_service_exp > 0 and rp["age"] < 65:
                    exp_under_65.append(resp_service_exp)
                    exp_under_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_general"] == "ANY PRIVATE":
                        private_exp_under_65.append(resp_service_exp)
                        private_exp_under_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_general"] == "PUBLIC ONLY":
                        public_exp_under_65.append(resp_service_exp)
                        public_exp_under_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_general"] == "UNINSURED":
                        uninsured_under_65.append(resp_service_exp)
                        uninsured_under_65_weight.append(rp["weight"])

                if resp_service_exp > 0 and rp["age"] >= 65:
                    exp_over_65.append(resp_service_exp)
                    exp_over_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_specific"] == "65+ EDITED MEDICARE ONLY":
                        medicare_exp_over_65.append(resp_service_exp)
                        medicare_exp_over_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_specific"] == "65+ EDITED MEDICARE AND PRIVATE":
                        medicare_private_exp_over_65.append(resp_service_exp)
                        medicare_private_exp_over_65_weight.append(rp["weight"])

                    if rp["insurance_coverage_specific"] == "65+ EDITED MEDICARE AND OTH PUB ONLY":
                        medicare_public_exp_over_65.append(resp_service_exp)
                        medicare_public_exp_over_65_weight.append(rp["weight"])

            for insurance_status, age_group, vals, weights in [
                ("all", "Under 65", exp_under_65, exp_under_65_weight),
                ("private", "Under 65", private_exp_under_65, private_exp_under_65_weight),
                ("public", "Under 65", public_exp_under_65, public_exp_under_65_weight),
                ("uninsured", "Under 65", uninsured_under_65, uninsured_under_65_weight),
                ("all", "Over 65", exp_over_65, exp_over_65_weight),
                ("medicare_only", "Over 65", medicare_exp_over_65, medicare_exp_over_65_weight),
                ("medicare_private", "Over 65", medicare_private_exp_over_65, medicare_private_exp_over_65_weight),
                ("medicare_public", "Over 65", medicare_public_exp_over_65, medicare_public_exp_over_65_weight),
            ]:
                expenses_insurance.append(
                    {
                        "year": year,
                        "insurance_status": insurance_status,
                        "age_group": age_group,
                        "mean": cpi.inflate(
                            uuf.weighted_average(values_list=vals, weights=weights), year, to=self.max_year
                        ),
                        "median": cpi.inflate(
                            uuf.weighted_median(values_list=vals, weights=weights), year, to=self.max_year
                        ),
                    }
                )

        return expenses_insurance

    def calculate_quantile_expenses(self):
        """ For the entire population, for each year calculates the total cumulative expenditures (in billions) and
        percent of total expenditures for all quantiles divisible by 10, in addition to the 75th, 95th and 99th
        quantile. Returns as a list of dictionaries. """

        quantile_expenses = []

        for year, population_characteristics in self.all_population_characteristics.items():
            year_expenditures, year_weights = [], []
            for resp_dict in population_characteristics.values():
                year_expenditures.append(resp_dict["characteristics"]["total_expenditures"])
                year_weights.append(resp_dict["characteristics"]["weight"])

            year_total_expenditures = sum([val * weight for val, weight in zip(year_expenditures, year_weights)])

            weighted_quantiles_dict = uuf.weighted_quantiles(
                values_list=year_expenditures,
                quantiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 0.99, 1],
                sample_weight=year_weights,
            )
            for quantile, val in weighted_quantiles_dict.items():
                quantile_member_exp, quantile_member_weights = [], []
                for exp, weight in zip(year_expenditures, year_weights):
                    if exp <= val:
                        quantile_member_exp.append(exp)
                        quantile_member_weights.append(weight)

                quantile_expenditures = sum(
                    [val * weight for val, weight in zip(quantile_member_exp, quantile_member_weights)]
                )

                quantile_expenses.append(
                    {
                        "year": year,
                        "quantile": quantile,
                        "cum_pct_exp": quantile_expenditures / year_total_expenditures * 100,
                        "total_exp": cpi.inflate(quantile_expenditures / 1000000000, year, to=self.max_year),
                    }
                )

        return quantile_expenses
