from meps_db.components.models.outpatient_visits_models import (
    OutpatientVisits18,
    OutpatientVisits17,
    OutpatientVisits16,
    OutpatientVisits15,
    OutpatientVisits14,
    OutpatientVisits13,
    OutpatientVisits12,
    OutpatientVisits11,
    OutpatientVisits10,
    OutpatientVisits09,
    OutpatientVisits08,
    OutpatientVisits07,
    OutpatientVisits06,
    OutpatientVisits05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder

class OutpatientVisitsEncoder(BaseEncoder):
    """  Queries the OutpatientVisits Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year=year
        self.dupersids=dupersids

        self.OP_LOOKUPS = {
            2018: {
                "model": OutpatientVisits18,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC_M18"},
                "see_doc": "SEEDOC_M18",            
            },
            2017: {
                "model": OutpatientVisits17,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2016: {
                "model": OutpatientVisits16,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2015: {
                "model": OutpatientVisits15,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2014: {
                "model": OutpatientVisits14,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2013: {
                "model": OutpatientVisits13,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2012: {
                "model": OutpatientVisits12,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2011: {
                "model": OutpatientVisits11,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2010: {
                "model": OutpatientVisits10,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2009: {
                "model": OutpatientVisits09,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2008: {
                "model": OutpatientVisits08,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2007: {
                "model": OutpatientVisits07,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2006: {
                "model": OutpatientVisits06,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2005: {
                "model": OutpatientVisits05,
                "fields": {"DUPERSID",  "EVNTIDX", "OPDATEYR", "OPDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
        }

    def run(self):
        """ Groups events by respondents. Classifies events that were associated with a physician. Return a list of 
        ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.OP_LOOKUPS[self.year]["model"].objects.filter(
                    DUPERSID__in=self.dupersids).values(*self.OP_LOOKUPS[self.year]["fields"]
                )
            )
        else:
            events = list(
                self.OP_LOOKUPS[self.year]["model"].objects.all().values(*self.OP_LOOKUPS[self.year]["fields"])
            )
            
        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["OPDATEYR"], month_str=event["OPDATEMM"]),
                    "physician_event": event[self.OP_LOOKUPS[self.year]["see_doc"]] in {"01"}
                }
            )
        
        respondents = self.order_histories(respondents=respondents)
        
        return respondents
