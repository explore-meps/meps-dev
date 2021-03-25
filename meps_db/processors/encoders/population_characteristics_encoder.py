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
                "fields": {
                    "DUPERSID",
                    "AGE18X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT18F",
                    "INSCOV18",
                    "INSURC18",
                    "DVTEXP18",
                    "ERTEXP18",
                    "HHAEXP18",
                    "HHNEXP18",
                    "IPTEXP18",
                    "OBVEXP18",
                    "OPTEXP18",
                    "OTHEXP18",
                    "RXEXP18",
                    "VISEXP18",
                    "TOTEXP18",
                },
                "age": "AGE18X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT18F",
                "insurance_coverage_general": "INSCOV18",
                "insurance_coverage_specific": "INSURC18",
                "dental_expenditures": "DVTEXP18",
                "emergency_room_expenditures": "ERTEXP18",
                "home_health_agency_expenditures": "HHAEXP18",
                "home_health_nonagency_expenditures": "HHNEXP18",
                "hospital_inpatient_expenditures": "IPTEXP18",
                "office_based_expenditures": "OBVEXP18",
                "outpatient_expenditures": "OPTEXP18",
                "other_medical_expenditures": "OTHEXP18",
                "prescription_medicine_expenditures": "RXEXP18",
                "vision_expenditures": "VISEXP18",
                "total_expenditures": "TOTEXP18",
            },
            2017: {
                "model": PopulationCharacteristics17,
                "fields": {
                    "DUPERSID",
                    "AGE17X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT17F",
                    "INSCOV17",
                    "INSURC17",
                    "DVTEXP17",
                    "ERTEXP17",
                    "HHAEXP17",
                    "HHNEXP17",
                    "IPTEXP17",
                    "OBVEXP17",
                    "OPTEXP17",
                    "OTHEXP17",
                    "RXEXP17",
                    "VISEXP17",
                    "TOTEXP17",
                },
                "age": "AGE17X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT17F",
                "insurance_coverage_general": "INSCOV17",
                "insurance_coverage_specific": "INSURC17",
                "dental_expenditures": "DVTEXP17",
                "emergency_room_expenditures": "ERTEXP17",
                "home_health_agency_expenditures": "HHAEXP17",
                "home_health_nonagency_expenditures": "HHNEXP17",
                "hospital_inpatient_expenditures": "IPTEXP17",
                "office_based_expenditures": "OBVEXP17",
                "outpatient_expenditures": "OPTEXP17",
                "other_medical_expenditures": "OTHEXP17",
                "prescription_medicine_expenditures": "RXEXP17",
                "vision_expenditures": "VISEXP17",
                "total_expenditures": "TOTEXP17",
            },
            2016: {
                "model": PopulationCharacteristics16,
                "fields": {
                    "DUPERSID",
                    "AGE16X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT16F",
                    "INSCOV16",
                    "INSURC16",
                    "DVTEXP16",
                    "ERTEXP16",
                    "HHAEXP16",
                    "HHNEXP16",
                    "IPTEXP16",
                    "OBVEXP16",
                    "OPTEXP16",
                    "OTHEXP16",
                    "RXEXP16",
                    "VISEXP16",
                    "TOTEXP16",
                },
                "age": "AGE16X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT16F",
                "insurance_coverage_general": "INSCOV16",
                "insurance_coverage_specific": "INSURC16",
                "dental_expenditures": "DVTEXP16",
                "emergency_room_expenditures": "ERTEXP16",
                "home_health_agency_expenditures": "HHAEXP16",
                "home_health_nonagency_expenditures": "HHNEXP16",
                "hospital_inpatient_expenditures": "IPTEXP16",
                "office_based_expenditures": "OBVEXP16",
                "outpatient_expenditures": "OPTEXP16",
                "other_medical_expenditures": "OTHEXP16",
                "prescription_medicine_expenditures": "RXEXP16",
                "vision_expenditures": "VISEXP16",
                "total_expenditures": "TOTEXP16",
            },
            2015: {
                "model": PopulationCharacteristics15,
                "fields": {
                    "DUPERSID",
                    "AGE15X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT15F",
                    "INSCOV15",
                    "INSURC15",
                    "DVTEXP15",
                    "ERTEXP15",
                    "HHAEXP15",
                    "HHNEXP15",
                    "IPTEXP15",
                    "OBVEXP15",
                    "OPTEXP15",
                    "OTHEXP15",
                    "RXEXP15",
                    "VISEXP15",
                    "TOTEXP15",
                },
                "age": "AGE15X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT15F",
                "insurance_coverage_general": "INSCOV15",
                "insurance_coverage_specific": "INSURC15",
                "dental_expenditures": "DVTEXP15",
                "emergency_room_expenditures": "ERTEXP15",
                "home_health_agency_expenditures": "HHAEXP15",
                "home_health_nonagency_expenditures": "HHNEXP15",
                "hospital_inpatient_expenditures": "IPTEXP15",
                "office_based_expenditures": "OBVEXP15",
                "outpatient_expenditures": "OPTEXP15",
                "other_medical_expenditures": "OTHEXP15",
                "prescription_medicine_expenditures": "RXEXP15",
                "vision_expenditures": "VISEXP15",
                "total_expenditures": "TOTEXP15",
            },
            2014: {
                "model": PopulationCharacteristics14,
                "fields": {
                    "DUPERSID",
                    "AGE14X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT14F",
                    "INSCOV14",
                    "INSURC14",
                    "DVTEXP14",
                    "ERTEXP14",
                    "HHAEXP14",
                    "HHNEXP14",
                    "IPTEXP14",
                    "OBVEXP14",
                    "OPTEXP14",
                    "OTHEXP14",
                    "RXEXP14",
                    "VISEXP14",
                    "TOTEXP14",
                },
                "age": "AGE14X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT14F",
                "insurance_coverage_general": "INSCOV14",
                "insurance_coverage_specific": "INSURC14",
                "dental_expenditures": "DVTEXP14",
                "emergency_room_expenditures": "ERTEXP14",
                "home_health_agency_expenditures": "HHAEXP14",
                "home_health_nonagency_expenditures": "HHNEXP14",
                "hospital_inpatient_expenditures": "IPTEXP14",
                "office_based_expenditures": "OBVEXP14",
                "outpatient_expenditures": "OPTEXP14",
                "other_medical_expenditures": "OTHEXP14",
                "prescription_medicine_expenditures": "RXEXP14",
                "vision_expenditures": "VISEXP14",
                "total_expenditures": "TOTEXP14",
            },
            2013: {
                "model": PopulationCharacteristics13,
                "fields": {
                    "DUPERSID",
                    "AGE13X",
                    "SEX",
                    "RACEV1X",
                    "RACEV2X",
                    "PERWT13F",
                    "INSCOV13",
                    "INSURC13",
                    "DVTEXP13",
                    "ERTEXP13",
                    "HHAEXP13",
                    "HHNEXP13",
                    "IPTEXP13",
                    "OBVEXP13",
                    "OPTEXP13",
                    "OTHEXP13",
                    "RXEXP13",
                    "VISEXP13",
                    "TOTEXP13",
                },
                "age": "AGE13X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": "RACEV2X",
                "weight": "PERWT13F",
                "insurance_coverage_general": "INSCOV13",
                "insurance_coverage_specific": "INSURC13",
                "dental_expenditures": "DVTEXP13",
                "emergency_room_expenditures": "ERTEXP13",
                "home_health_agency_expenditures": "HHAEXP13",
                "home_health_nonagency_expenditures": "HHNEXP13",
                "hospital_inpatient_expenditures": "IPTEXP13",
                "office_based_expenditures": "OBVEXP13",
                "outpatient_expenditures": "OPTEXP13",
                "other_medical_expenditures": "OTHEXP13",
                "prescription_medicine_expenditures": "RXEXP13",
                "vision_expenditures": "VISEXP13",
                "total_expenditures": "TOTEXP13",
            },
            2012: {
                "model": PopulationCharacteristics12,
                "fields": {
                    "DUPERSID",
                    "AGE12X",
                    "SEX",
                    "RACEV1X",
                    "PERWT12F",
                    "INSCOV12",
                    "INSURC12",
                    "DVTEXP12",
                    "ERTEXP12",
                    "HHAEXP12",
                    "HHNEXP12",
                    "IPTEXP12",
                    "OBVEXP12",
                    "OPTEXP12",
                    "OTHEXP12",
                    "RXEXP12",
                    "VISEXP12",
                    "TOTEXP12",
                },
                "age": "AGE12X",
                "race_v0": None,
                "race_v1": "RACEV1X",
                "race_v2": None,
                "weight": "PERWT12F",
                "insurance_coverage_general": "INSCOV12",
                "insurance_coverage_specific": "INSURC12",
                "dental_expenditures": "DVTEXP12",
                "emergency_room_expenditures": "ERTEXP12",
                "home_health_agency_expenditures": "HHAEXP12",
                "home_health_nonagency_expenditures": "HHNEXP12",
                "hospital_inpatient_expenditures": "IPTEXP12",
                "office_based_expenditures": "OBVEXP12",
                "outpatient_expenditures": "OPTEXP12",
                "other_medical_expenditures": "OTHEXP12",
                "prescription_medicine_expenditures": "RXEXP12",
                "vision_expenditures": "VISEXP12",
                "total_expenditures": "TOTEXP12",
            },
            2011: {
                "model": PopulationCharacteristics11,
                "fields": {
                    "DUPERSID",
                    "AGE11X",
                    "SEX",
                    "RACEX",
                    "PERWT11F",
                    "INSCOV11",
                    "INSURC11",
                    "DVTEXP11",
                    "ERTEXP11",
                    "HHAEXP11",
                    "HHNEXP11",
                    "IPTEXP11",
                    "OBVEXP11",
                    "OPTEXP11",
                    "OTHEXP11",
                    "RXEXP11",
                    "VISEXP11",
                    "TOTEXP11",
                },
                "age": "AGE11X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT11F",
                "insurance_coverage_general": "INSCOV11",
                "insurance_coverage_specific": "INSURC11",
                "dental_expenditures": "DVTEXP11",
                "emergency_room_expenditures": "ERTEXP11",
                "home_health_agency_expenditures": "HHAEXP11",
                "home_health_nonagency_expenditures": "HHNEXP11",
                "hospital_inpatient_expenditures": "IPTEXP11",
                "office_based_expenditures": "OBVEXP11",
                "outpatient_expenditures": "OPTEXP11",
                "other_medical_expenditures": "OTHEXP11",
                "prescription_medicine_expenditures": "RXEXP11",
                "vision_expenditures": "VISEXP11",
                "total_expenditures": "TOTEXP11",
            },
            2010: {
                "model": PopulationCharacteristics10,
                "fields": {
                    "DUPERSID",
                    "AGE10X",
                    "SEX",
                    "RACEX",
                    "PERWT10F",
                    "INSCOV10",
                    "DVTEXP10",
                    "PRVEV10",
                    "TRIEV10",
                    "MCDEV10",
                    "MCREV10",
                    "OPAEV10",
                    "OPBEV10",
                    "UNINS10",
                    "ERTEXP10",
                    "HHAEXP10",
                    "HHNEXP10",
                    "IPTEXP10",
                    "OBVEXP10",
                    "OPTEXP10",
                    "OTHEXP10",
                    "RXEXP10",
                    "VISEXP10",
                    "TOTEXP10",
                },
                "age": "AGE10X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT10F",
                "insurance_coverage_general": "INSCOV10",
                "ever_had_medicaid": "MCDEV10",
                "ever_had_private": "PRVEV10",
                "ever_had_tricare": "TRIEV10",
                "ever_had_medicare": "MCREV10",
                "ever_had_public_a": "OPAEV10",
                "ever_had_public_b": "OPBEV10",
                "uninsured": "UNINS10",
                "dental_expenditures": "DVTEXP10",
                "emergency_room_expenditures": "ERTEXP10",
                "home_health_agency_expenditures": "HHAEXP10",
                "home_health_nonagency_expenditures": "HHNEXP10",
                "hospital_inpatient_expenditures": "IPTEXP10",
                "office_based_expenditures": "OBVEXP10",
                "outpatient_expenditures": "OPTEXP10",
                "other_medical_expenditures": "OTHEXP10",
                "prescription_medicine_expenditures": "RXEXP10",
                "vision_expenditures": "VISEXP10",
                "total_expenditures": "TOTEXP10",
            },
            2009: {
                "model": PopulationCharacteristics09,
                "fields": {
                    "DUPERSID",
                    "AGE09X",
                    "SEX",
                    "RACEX",
                    "PERWT09F",
                    "INSCOV09",
                    "PRVEV09",
                    "TRIEV09",
                    "MCDEV09",
                    "MCREV09",
                    "OPAEV09",
                    "OPBEV09",
                    "UNINS09",
                    "DVTEXP09",
                    "ERTEXP09",
                    "HHAEXP09",
                    "HHNEXP09",
                    "IPTEXP09",
                    "OBVEXP09",
                    "OPTEXP09",
                    "OTHEXP09",
                    "RXEXP09",
                    "VISEXP09",
                    "TOTEXP09",
                },
                "age": "AGE09X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT09F",
                "insurance_coverage_general": "INSCOV09",
                "ever_had_medicaid": "MCDEV09",
                "ever_had_private": "PRVEV09",
                "ever_had_tricare": "TRIEV09",
                "ever_had_medicare": "MCREV09",
                "ever_had_public_a": "OPAEV09",
                "ever_had_public_b": "OPBEV09",
                "uninsured": "UNINS09",
                "dental_expenditures": "DVTEXP09",
                "emergency_room_expenditures": "ERTEXP09",
                "home_health_agency_expenditures": "HHAEXP09",
                "home_health_nonagency_expenditures": "HHNEXP09",
                "hospital_inpatient_expenditures": "IPTEXP09",
                "office_based_expenditures": "OBVEXP09",
                "outpatient_expenditures": "OPTEXP09",
                "other_medical_expenditures": "OTHEXP09",
                "prescription_medicine_expenditures": "RXEXP09",
                "vision_expenditures": "VISEXP09",
                "total_expenditures": "TOTEXP09",
            },
            2008: {
                "model": PopulationCharacteristics08,
                "fields": {
                    "DUPERSID",
                    "AGE08X",
                    "SEX",
                    "RACEX",
                    "PERWT08F",
                    "INSCOV08",
                    "PRVEV08",
                    "TRIEV08",
                    "MCDEV08",
                    "MCREV08",
                    "OPAEV08",
                    "OPBEV08",
                    "UNINS08",
                    "DVTEXP08",
                    "ERTEXP08",
                    "HHAEXP08",
                    "HHNEXP08",
                    "IPTEXP08",
                    "OBVEXP08",
                    "OPTEXP08",
                    "OTHEXP08",
                    "RXEXP08",
                    "VISEXP08",
                    "TOTEXP08",
                },
                "age": "AGE08X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT08F",
                "insurance_coverage_general": "INSCOV08",
                "ever_had_medicaid": "MCDEV08",
                "ever_had_private": "PRVEV08",
                "ever_had_tricare": "TRIEV08",
                "ever_had_medicare": "MCREV08",
                "ever_had_public_a": "OPAEV08",
                "ever_had_public_b": "OPBEV08",
                "uninsured": "UNINS08",
                "dental_expenditures": "DVTEXP08",
                "emergency_room_expenditures": "ERTEXP08",
                "home_health_agency_expenditures": "HHAEXP08",
                "home_health_nonagency_expenditures": "HHNEXP08",
                "hospital_inpatient_expenditures": "IPTEXP08",
                "office_based_expenditures": "OBVEXP08",
                "outpatient_expenditures": "OPTEXP08",
                "other_medical_expenditures": "OTHEXP08",
                "prescription_medicine_expenditures": "RXEXP08",
                "vision_expenditures": "VISEXP08",
                "total_expenditures": "TOTEXP08",
            },
            2007: {
                "model": PopulationCharacteristics07,
                "fields": {
                    "DUPERSID",
                    "AGE07X",
                    "SEX",
                    "RACEX",
                    "PERWT07F",
                    "INSCOV07",
                    "PRVEV07",
                    "TRIEV07",
                    "MCDEV07",
                    "MCREV07",
                    "OPAEV07",
                    "OPBEV07",
                    "UNINS07",
                    "DVTEXP07",
                    "ERTEXP07",
                    "HHAEXP07",
                    "HHNEXP07",
                    "IPTEXP07",
                    "OBVEXP07",
                    "OPTEXP07",
                    "OTHEXP07",
                    "RXEXP07",
                    "VISEXP07",
                    "TOTEXP07",
                },
                "age": "AGE07X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT07F",
                "insurance_coverage_general": "INSCOV07",
                "ever_had_medicaid": "MCDEV07",
                "ever_had_private": "PRVEV07",
                "ever_had_tricare": "TRIEV07",
                "ever_had_medicare": "MCREV07",
                "ever_had_public_a": "OPAEV07",
                "ever_had_public_b": "OPBEV07",
                "uninsured": "UNINS07",
                "dental_expenditures": "DVTEXP07",
                "emergency_room_expenditures": "ERTEXP07",
                "home_health_agency_expenditures": "HHAEXP07",
                "home_health_nonagency_expenditures": "HHNEXP07",
                "hospital_inpatient_expenditures": "IPTEXP07",
                "office_based_expenditures": "OBVEXP07",
                "outpatient_expenditures": "OPTEXP07",
                "other_medical_expenditures": "OTHEXP07",
                "prescription_medicine_expenditures": "RXEXP07",
                "vision_expenditures": "VISEXP07",
                "total_expenditures": "TOTEXP07",
            },
            2006: {
                "model": PopulationCharacteristics06,
                "fields": {
                    "DUPERSID",
                    "AGE06X",
                    "SEX",
                    "RACEX",
                    "PERWT06F",
                    "INSCOV06",
                    "PRVEV06",
                    "TRIEV06",
                    "MCDEV06",
                    "MCREV06",
                    "OPAEV06",
                    "OPBEV06",
                    "UNINS06",
                    "DVTEXP06",
                    "ERTEXP06",
                    "HHAEXP06",
                    "HHNEXP06",
                    "IPTEXP06",
                    "OBVEXP06",
                    "OPTEXP06",
                    "OTHEXP06",
                    "RXEXP06",
                    "VISEXP06",
                    "TOTEXP06",
                },
                "age": "AGE06X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT06F",
                "insurance_coverage_general": "INSCOV06",
                "ever_had_medicaid": "MCDEV06",
                "ever_had_private": "PRVEV06",
                "ever_had_tricare": "TRIEV06",
                "ever_had_medicare": "MCREV06",
                "ever_had_public_a": "OPAEV06",
                "ever_had_public_b": "OPBEV06",
                "uninsured": "UNINS06",
                "dental_expenditures": "DVTEXP06",
                "emergency_room_expenditures": "ERTEXP06",
                "home_health_agency_expenditures": "HHAEXP06",
                "home_health_nonagency_expenditures": "HHNEXP06",
                "hospital_inpatient_expenditures": "IPTEXP06",
                "office_based_expenditures": "OBVEXP06",
                "outpatient_expenditures": "OPTEXP06",
                "other_medical_expenditures": "OTHEXP06",
                "prescription_medicine_expenditures": "RXEXP06",
                "vision_expenditures": "VISEXP06",
                "total_expenditures": "TOTEXP06",
            },
            2005: {
                "model": PopulationCharacteristics05,
                "fields": {
                    "DUPERSID",
                    "AGE05X",
                    "SEX",
                    "RACEX",
                    "PERWT05F",
                    "INSCOV05",
                    "PRVEV05",
                    "TRIEV05",
                    "MCDEV05",
                    "MCREV05",
                    "OPAEV05",
                    "OPBEV05",
                    "UNINS05",
                    "DVTEXP05",
                    "ERTEXP05",
                    "HHAEXP05",
                    "HHNEXP05",
                    "IPTEXP05",
                    "OBVEXP05",
                    "OPTEXP05",
                    "OTHEXP05",
                    "RXEXP05",
                    "VISEXP05",
                    "TOTEXP05",
                },
                "age": "AGE05X",
                "race_v0": "RACEX",
                "race_v1": None,
                "race_v2": None,
                "weight": "PERWT05F",
                "insurance_coverage_general": "INSCOV05",
                "ever_had_medicaid": "MCDEV05",
                "ever_had_private": "PRVEV05",
                "ever_had_tricare": "TRIEV05",
                "ever_had_medicare": "MCREV05",
                "ever_had_public_a": "OPAEV05",
                "ever_had_public_b": "OPBEV05",
                "uninsured": "UNINS05",
                "dental_expenditures": "DVTEXP05",
                "emergency_room_expenditures": "ERTEXP05",
                "home_health_agency_expenditures": "HHAEXP05",
                "home_health_nonagency_expenditures": "HHNEXP05",
                "hospital_inpatient_expenditures": "IPTEXP05",
                "office_based_expenditures": "OBVEXP05",
                "outpatient_expenditures": "OPTEXP05",
                "other_medical_expenditures": "OTHEXP05",
                "prescription_medicine_expenditures": "RXEXP05",
                "vision_expenditures": "VISEXP05",
                "total_expenditures": "TOTEXP05",
            },
        }

        self.RACE_V0_ENCODER = {
            "1": "WHITE - NO OTHER RACE REPORTED",
            "2": "BLACK - NO OTHER RACE REPORTED",
            "3": "AMER INDIAN/ALASKA NATIVE - NO OTH RAC",
            "4": "ASIAN - NO OTHER RACE REPORTE",
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
        self.COVERAGE_GENERAL = {
            "1": "ANY PRIVATE",
            "2": "PUBLIC ONLY",
            "3": "UNINSURED",
        }
        self.COVERAGE_SPECIFIC = {
            "1": "<65 ANY PRIVATE",
            "2": "<65 PUBLIC ONLY",
            "3": "<65 UNINSURED",
            "4": "65+ EDITED MEDICARE ONLY",
            "5": "65+ EDITED MEDICARE AND PRIVATE",
            "6": "65+ EDITED MEDICARE AND OTH PUB ONLY",
            "7": "65+ UNINSURED",
            "8": "65+ NO MEDICARE AND ANY PUBLIC/PRIVATE",
        }

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

            # fetch data
            age = data[self.PC_LOOKUPS[self.year]["age"]]
            sex = data["SEX"]
            weight = data[self.PC_LOOKUPS[self.year]["weight"]]
            race_v0 = data.get(self.PC_LOOKUPS[self.year]["race_v0"], None)
            race_v1 = data.get(self.PC_LOOKUPS[self.year]["race_v1"], None)
            race_v2 = data.get(self.PC_LOOKUPS[self.year]["race_v2"], None)

            insurance_coverage_general = data.get(self.PC_LOOKUPS[self.year]["insurance_coverage_general"], None)
            insurance_coverage_specific = self.calculate_insurance_cov_specific(data=data)

            dental_expenditures = data[self.PC_LOOKUPS[self.year]["dental_expenditures"]]
            emergency_room_expenditures = data[self.PC_LOOKUPS[self.year]["emergency_room_expenditures"]]
            home_health_agency_expenditures = data[self.PC_LOOKUPS[self.year]["home_health_agency_expenditures"]]
            home_health_nonagency_expenditures = data[self.PC_LOOKUPS[self.year]["home_health_nonagency_expenditures"]]
            hospital_inpatient_expenditures = data[self.PC_LOOKUPS[self.year]["hospital_inpatient_expenditures"]]
            office_based_expenditures = data[self.PC_LOOKUPS[self.year]["office_based_expenditures"]]
            outpatient_expenditures = data[self.PC_LOOKUPS[self.year]["outpatient_expenditures"]]
            other_medical_expenditures = data[self.PC_LOOKUPS[self.year]["other_medical_expenditures"]]
            prescription_medicine_expenditures = data[self.PC_LOOKUPS[self.year]["prescription_medicine_expenditures"]]
            vision_expenditures = data[self.PC_LOOKUPS[self.year]["vision_expenditures"]]
            total_expenditures = data[self.PC_LOOKUPS[self.year]["total_expenditures"]]

            # enocoders only
            population[resp_id] = {
                "characteristics": {
                    "resp_id": resp_id,
                    "age": float(age),
                    "sex": self.SEX_ENCODER.get(sex),
                    "weight": float(weight),
                    "race_v0": self.RACE_V0_ENCODER.get(race_v0),
                    "race_v1": self.RACE_V1_ENCODER.get(race_v1),
                    "race_v2": self.RACE_V2_ENCODER.get(race_v2),
                    "insurance_coverage_general": self.COVERAGE_GENERAL.get(insurance_coverage_general),
                    "insurance_coverage_specific": self.COVERAGE_SPECIFIC.get(insurance_coverage_specific),
                    "dental_expenditures": float(dental_expenditures),
                    "emergency_room_expenditures": float(emergency_room_expenditures),
                    "home_health_agency_expenditures": float(home_health_agency_expenditures),
                    "home_health_nonagency_expenditures": float(home_health_nonagency_expenditures),
                    "hospital_inpatient_expenditures": float(hospital_inpatient_expenditures),
                    "office_based_expenditures": float(office_based_expenditures),
                    "outpatient_expenditures": float(outpatient_expenditures),
                    "other_medical_expenditures": float(other_medical_expenditures),
                    "prescription_medicine_expenditures": float(prescription_medicine_expenditures),
                    "vision_expenditures": float(vision_expenditures),
                    "total_expenditures": float(total_expenditures),
                }
            }

        return population

    def calculate_insurance_cov_specific(self, data):
        """ 
            Extracts the INSCOV*YY* variable for years after 2010, for years 2010 and earlier, rebuilds the INSCOV*YY*
            from its component parts. Returns a string value intended for use with the following map:
        
                "1": "<65 ANY PRIVATE",	
                "2": "<65 PUBLIC ONLY",	
                "3": "<65 UNINSURED",	
                "4": "65+ EDITED MEDICARE ONLY",	
                "5": "65+ EDITED MEDICARE AND PRIVATE",	
                "6": "65+ EDITED MEDICARE AND OTH PUB ONLY",	
                "7": "65+ UNINSURED",
                "8": "65+ NO MEDICARE AND ANY PUBLIC/PRIVATE",	

        """

        # pre 2010 is accounted for
        if self.year > 2010:
            return data.get(self.PC_LOOKUPS[self.year]["insurance_coverage_specific"])

        # under 65s is just insurance_coverage_general
        if float(data.get(self.PC_LOOKUPS[self.year]["age"])) < 65:
            return data.get(self.PC_LOOKUPS[self.year]["insurance_coverage_general"])

        # calculate medicare only
        if (
            data.get(self.PC_LOOKUPS[self.year]["ever_had_medicare"]) == "1"
            and data.get(self.PC_LOOKUPS[self.year]["ever_had_private"]) == "2"
            and data.get(self.PC_LOOKUPS[self.year]["ever_had_tricare"]) == "2"
            and data.get(self.PC_LOOKUPS[self.year]["ever_had_medicaid"]) == "2"
            and data.get(self.PC_LOOKUPS[self.year]["ever_had_public_a"]) == "2"
            and data.get(self.PC_LOOKUPS[self.year]["ever_had_public_b"]) == "2"
            and data.get(self.PC_LOOKUPS[self.year]["uninsured"]) == "2"
        ):
            return "4"

        # calculate medicare and private
        if data.get(self.PC_LOOKUPS[self.year]["ever_had_medicare"]) == "1" and (
            data.get(self.PC_LOOKUPS[self.year]["ever_had_private"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_tricare"]) == "1"
        ):
            return "5"

        # calculate medicare and public
        if data.get(self.PC_LOOKUPS[self.year]["ever_had_medicare"]) == "1" and (
            data.get(self.PC_LOOKUPS[self.year]["ever_had_medicaid"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_public_a"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_public_b"]) == "1"
        ):
            return "6"

        # calculate uninsured
        if data.get(self.PC_LOOKUPS[self.year]["uninsured"]) == "1":
            return "7"

        # calculate no medicare and any private or public
        if data.get(self.PC_LOOKUPS[self.year]["ever_had_medicare"]) == "2" and (
            data.get(self.PC_LOOKUPS[self.year]["ever_had_private"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_tricare"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_medicaid"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_public_a"]) == "1"
            or data.get(self.PC_LOOKUPS[self.year]["ever_had_public_b"]) == "1"
        ):
            return "8"
