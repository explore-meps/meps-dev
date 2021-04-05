from meps_db.components.models.office_based_visits_models import (
    OfficeBasedVisits18,
    OfficeBasedVisits17,
    OfficeBasedVisits16,
    OfficeBasedVisits15,
    OfficeBasedVisits14,
    OfficeBasedVisits13,
    OfficeBasedVisits12,
    OfficeBasedVisits11,
    OfficeBasedVisits10,
    OfficeBasedVisits09,
    OfficeBasedVisits08,
    OfficeBasedVisits07,
    OfficeBasedVisits06,
    OfficeBasedVisits05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class OfficeBasedVisitsEncoder(BaseEncoder):
    """  Queries the OfficeBasedVisits Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.OB_LOOKUPS = {
            2018: {
                "model": OfficeBasedVisits18,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC_M18", "DRSPLTY_M18"},
                "see_doc": "SEEDOC_M18",
                "specialty": "DRSPLTY_M18"
            },
            2017: {
                "model": OfficeBasedVisits17,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2016: {
                "model": OfficeBasedVisits16,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2015: {
                "model": OfficeBasedVisits15,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2014: {
                "model": OfficeBasedVisits14,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2013: {
                "model": OfficeBasedVisits13,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2012: {
                "model": OfficeBasedVisits12,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2011: {
                "model": OfficeBasedVisits11,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2010: {
                "model": OfficeBasedVisits10,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2009: {
                "model": OfficeBasedVisits09,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2008: {
                "model": OfficeBasedVisits08,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2007: {
                "model": OfficeBasedVisits07,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2006: {
                "model": OfficeBasedVisits06,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
            2005: {
                "model": OfficeBasedVisits05,
                "fields": {"DUPERSID", "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC", "DRSPLTY",},
                "see_doc": "SEEDOC",
                "specialty": "DRSPLTY",
            },
        }
    
        self.SPECIALTY_ENCODER = {
            "01": "ALLERGY/IMMUNOLOGY",	
            "02": "ANESTHESIOLOGY",	
            "03": "CARDIOLOGY", 
            "04": "DERMATOLOGY", 
            "05": "ENDOCRINOLOGY/METABOLISM",	
            "06": "FAMILY PRACTICE",	
            "07": "GASTROENTEROLOGY",	
            "08": "GENERAL PRACTICE",	
            "09": "GENERAL SURGERY",	
            "10": "GERIATRICS", 
            "11": "GYNECOLOGY/OBSTETRICS",	
            "12": "HEMATOLOGY",
            "13": "HOSPITAL RESIDENCE",	
            "14": "INTERNAL MEDICINE",	
            "15": "NEPHROLOGY", 
            "16": "NEUROLOGY",	
            "18": "ONCOLOGY",	
            "19": "OPHTHALMOLOGY",	
            "20": "ORTHOPEDICS",	
            "21": "OSTEOPATHY",	
            "22": "OTORHINOLARYNGOLOGY",	
            "23": "PATHOLOGY",	
            "24": "PEDIATRICIAN",	
            "25": "PHYSICAL MEDICINE/REHAB",	
            "26": "PLASTIC SURGERY",	
            "27": "PROCTOLOGY",
            "28": "PSYCHIATRY",	
            "29": "PULMONARY",	
            "30": "RADIOLOGY",	
            "31": "RHEUMATOLOGY",
            "32": "THORACIC SURGERY",	
            "33": "UROLOGY",	
            "91": "OTHER DR SPECIALTY",
        }

    def run(self):
        """ Groups events by respondents. Classifies events that were associated with a physician. Return a list of
        ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.OB_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.OB_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.OB_LOOKUPS[self.year]["model"].objects.all().values(*self.OB_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []

            primary_care = self.SPECIALTY_ENCODER.get(event[self.OB_LOOKUPS[self.year]["specialty"]]) in {
                "GENERAL PRACTICE", "FAMILY PRACTICE", "INTERNAL MEDICINE"
            }

            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["OBDATEYR"], month_str=event["OBDATEMM"]),
                    "physician_event": event[self.OB_LOOKUPS[self.year]["see_doc"]] in {"01"},
                    "primary_care_event": primary_care,
                    "doctor_specialty": self.SPECIALTY_ENCODER.get(event[self.OB_LOOKUPS[self.year]["specialty"]])
                }
            )

        respondents = self.order_histories(respondents=respondents)

        return respondents
