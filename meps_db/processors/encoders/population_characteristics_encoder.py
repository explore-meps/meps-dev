from meps_db.components.models.population_characteristics_models import (
    PopulationCharacteristics18,
    PopulationCharacteristics17,
    PopulationCharacteristics16,
    PopulationCharacteristics15,
    PopulationCharacteristics14,
    PopulationCharacteristics13,
    PopulationCharacteristics12,
    PopulationCharacteristics11,
    PopulationCharacteristics10,
    PopulationCharacteristics09,
    PopulationCharacteristics08,
    PopulationCharacteristics07,
    PopulationCharacteristics06,
    PopulationCharacteristics05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class PopulationCharacteristicsEncoder(BaseEncoder):
    """  Queries the PopulationCharacteristics Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.PC_LOOKUPS = {
            2018: {
                "model": PopulationCharacteristics18,
                "fields": {"DUPERSID", "AGE18X", "SEX", "RACEV1X", "RACEV2X", "PERWT18F"},
                "age": "AGE18X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT18F",
            },
            2017: {
                "model": PopulationCharacteristics17,
                "fields": {"DUPERSID", "AGE17X", "SEX", "RACEV1X", "RACEV2X", "PERWT17F"},
                "age": "AGE17X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT17F",
            },
            2016: {
                "model": PopulationCharacteristics16,
                "fields": {"DUPERSID", "AGE16X", "SEX", "RACEV1X", "RACEV2X", "PERWT16F"},
                "age": "AGE16X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT16F",
            },
            2015: {
                "model": PopulationCharacteristics15,
                "fields": {"DUPERSID", "AGE15X", "SEX", "RACEV1X", "RACEV2X", "PERWT15F"},
                "age": "AGE15X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT15F",
            },
            2014: {
                "model": PopulationCharacteristics14,
                "fields": {"DUPERSID", "AGE14X", "SEX", "RACEV1X", "RACEV2X", "PERWT14F"},
                "age": "AGE14X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT14F",
            },
            2013: {
                "model": PopulationCharacteristics13,
                "fields": {"DUPERSID", "AGE13X", "SEX", "RACEV1X", "RACEV2X", "PERWT13F"},
                "age": "AGE13X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT13F",
            },
            2012: {
                "model": PopulationCharacteristics12,
                "fields": {"DUPERSID", "AGE12X", "SEX", "RACEV1X", "PERWT12F"},
                "age": "AGE12X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": None,
                "weight": "PERWT12F",
            },
            2011: {
                "model": PopulationCharacteristics11,
                "fields": {"DUPERSID", "AGE11X", "SEX", "RACEX", "PERWT11F"},
                "age": "AGE11X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT11F",
            },
            2010: {
                "model": PopulationCharacteristics10,
                "fields": {"DUPERSID", "AGE10X", "SEX", "RACEX", "PERWT10F"},
                "age": "AGE10X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT10F",
            },
            2009: {
                "model": PopulationCharacteristics09,
                "fields": {"DUPERSID", "AGE09X", "SEX", "RACEX", "PERWT09F"},
                "age": "AGE09X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT09F",
            },
            2008: {
                "model": PopulationCharacteristics08,
                "fields": {"DUPERSID", "AGE08X", "SEX", "RACEX", "PERWT08F"},
                "age": "AGE08X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT08F",
            },
            2007: {
                "model": PopulationCharacteristics07,
                "fields": {"DUPERSID", "AGE07X", "SEX", "RACEX", "PERWT07F"},
                "age": "AGE07X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT07F",
            },
            2006: {
                "model": PopulationCharacteristics06,
                "fields": {"DUPERSID", "AGE06X", "SEX", "RACEX", "PERWT06F"},
                "age": "AGE06X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT06F",
            },
            2005: {
                "model": PopulationCharacteristics05,
                "fields": {"DUPERSID", "AGE05X", "SEX", "RACEX", "PERWT05F"},
                "age": "AGE05X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT05F",
            },
        }

        self.RACE_V0_ENCODER = {
            "1": "WHITE - NO OTHER RACE REPORTED",
            "2": "BLACK - NO OTHER RACE REPORTED",
            "3": "AMER INDIAN/ALASKA NATIVE - NO OTH RAC",
            "4": "ASIAN - NO OTHER RACE REPORTED",
            "5": "NATIVE HAWAIIAN/PACIFIC ISLANDER-NO OTHR",
            "6": "MULTIPLE RACES REPORTED",
        }

        self.RACE_V1_ENCODER = {
            "1": "WHITE - NO OTHER RACE REPORTED",
            "2": "BLACK - NO OTHER RACE REPORTED",
            "3": "AMER INDIAN/ALASKA NATIVE-NO OTHER RACE",
            "4": "ASIAN/NATV HAWAIIAN/PACFC ISL-NO OTH",
            "6": "MULTIPLE RACES REPORTED",
        }

        self.RACE_V2_ENCODER = {
            "01": "WHITE - NO OTHER RACE REPORTED",
            "02": "BLACK - NO OTHER RACE REPORTED",
            "03": "AMER INDIAN/ALASKA NATIVE-NO OTHER RACE",
            "04": "ASIAN INDIAN - NO OTHER RACE REPORTED",
            "05": "CHINESE - NO OTHER RACE REPORTED",
            "06": "FILIPINO - NO OTHER RACE REPORTED",
            "10": "OTH ASIAN/NATV HAWAIIAN/PACFC ISL-NO OTH",
            "12": "MULTIPLE RACES REPORTED",
        }

        self.SEX_ENCODER = {"1": "MALE", "2": "FEMALE"}

    def run(self):
        """ Fetches all respondents for a year. Stores basic characteristics. 
        Variable Descriptions:
            resp_id: DUPERSID of respondent
            age: Age as of 12/31/YEAR
            sex: either of the two main categories (male and female) divided on the basis of reproductive function
            race: description of respondent ethnicity
            weight: respondents sample weight with respect to the US population 
        Variable Evolutions:
            race_0: used from 2002-2011, 5 categories, consistent throughout use
            race_1: used since 2012, 5-6 categories, Asian and Pacific Islander we seperated only in 2012
            race_2: used since 2013, 9 categories, from 2013-2015 people with multiple Asian races or multiple
                Hawaiian/Pacific Islander races were considered multiple races, from 2016 on persons with multiple 
                Asian races or multiple Hawaiian/Pacific Islander races were no longer considered multiple races
        """

        if self.dupersids:
            respondents_data = list(
                self.PC_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.PC_LOOKUPS[self.year]["fields"])
            )
        else:
            respondents_data = list(
                self.PC_LOOKUPS[self.year]["model"].objects.all().values(*self.PC_LOOKUPS[self.year]["fields"])
            )
        population = {}
        for data in respondents_data:
            resp_id = data["DUPERSID"]
            population[resp_id] = {
                "characteristics": {
                    "resp_id": resp_id,
                    "age": float(data[self.PC_LOOKUPS[self.year]["age"]]),
                    "sex": self.SEX_ENCODER.get(data["SEX"]),
                    "race_v0": self.RACE_V0_ENCODER.get(data.get(self.PC_LOOKUPS[self.year]["race_v0"], None)),
                    "race_v1": self.RACE_V1_ENCODER.get(data.get(self.PC_LOOKUPS[self.year]["race_v1"], None)),
                    "race_v2": self.RACE_V2_ENCODER.get(data.get(self.PC_LOOKUPS[self.year]["race_v2"], None)),
                    "weight": float(data[self.PC_LOOKUPS[self.year]["weight"]]),
                }
            }
        return population
