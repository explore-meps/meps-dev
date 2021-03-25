import numpy as np

import cpi

from meps_db.processors.encoders.population_characteristics_encoder import PopulationCharacteristicsEncoder


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
                            "pct_with_expenses": self.weighted_pct(bool_list=values, weights=weights),
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
                                self.weighted_average(values_list=values, weights=weights), year, to=self.max_year
                            ),
                            "median": cpi.inflate(
                                self.weighted_median(data=values, weights=weights), year, to=self.max_year
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
                            self.weighted_average(values_list=vals, weights=weights), year, to=self.max_year
                        ),
                        "median": cpi.inflate(
                            self.weighted_median(data=vals, weights=weights), year, to=self.max_year
                        ),
                    }
                )

        return expenses_insurance

    @staticmethod
    def weighted_pct(bool_list, weights):
        """ Takes a list of boolean values and a list of weights associated by index. Returns the percent of the
        weighted population listed a True in the boolean list. """

        numerator = 0
        for val, weight in zip(bool_list, weights):
            numerator += val * weight
        denominator = sum(weights)

        return numerator / denominator * 100

    @staticmethod
    def weighted_average(values_list, weights):
        """ Takes a list of values and a list of weights associated by index. Returns the weighted average of the 
        values. """

        numerator = 0
        for val, weight in zip(values_list, weights):
            numerator += val * weight
        denominator = sum(weights)

        return numerator / denominator

    @staticmethod
    def weighted_median(data, weights):
        """ Takes a list of values and a list of weights associated by index. Returns the weighted median of the 
        values. """
        data, weights = np.array(data).squeeze(), np.array(weights).squeeze()
        s_data, s_weights = map(np.array, zip(*sorted(zip(data, weights))))
        midpoint = 0.5 * sum(s_weights)
        if any(weights > midpoint):
            w_median = (data[weights == np.max(weights)])[0]
        else:
            cs_weights = np.cumsum(s_weights)
            idx = np.where(cs_weights <= midpoint)[0][-1]
            if cs_weights[idx] == midpoint:
                w_median = np.mean(s_data[idx : idx + 2])
            else:
                w_median = s_data[idx + 1]
        return w_median
