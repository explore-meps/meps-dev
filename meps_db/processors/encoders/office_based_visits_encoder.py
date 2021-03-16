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

        self.year=year
        self.dupersids=dupersids

        self.OB_LOOKUPS = {
            2018: {
                "model": OfficeBasedVisits18,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC_M18"},
                "see_doc": "SEEDOC_M18",
            },
            2017: {
                "model": OfficeBasedVisits17,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2016: {
                "model": OfficeBasedVisits16,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2015: {
                "model": OfficeBasedVisits15,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2014: {
                "model": OfficeBasedVisits14,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2013: {
                "model": OfficeBasedVisits13,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2012: {
                "model": OfficeBasedVisits12,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2011: {
                "model": OfficeBasedVisits11,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2010: {
                "model": OfficeBasedVisits10,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2009: {
                "model": OfficeBasedVisits09,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2008: {
                "model": OfficeBasedVisits08,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2007: {
                "model": OfficeBasedVisits07,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2006: {
                "model": OfficeBasedVisits06,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
            2005: {
                "model": OfficeBasedVisits05,
                "fields": {"DUPERSID",  "EVNTIDX", "OBDATEYR", "OBDATEMM", "SEEDOC",},
                "see_doc": "SEEDOC",
            },
        }

    def run(self):
        """ Groups events by respondents. Classifies events that were associated with a physician. Return a list of
        ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.OB_LOOKUPS[self.year]["model"].objects.filter(
                    DUPERSID__in=self.dupersids).values(*self.OB_LOOKUPS[self.year]["fields"]
                )
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
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["OBDATEYR"], month_str=event["OBDATEMM"]),
                    "physician_event": event[self.OB_LOOKUPS[self.year]["see_doc"]] in {"01"}
                }
            )
        
        respondents = self.order_histories(respondents=respondents)

        return respondents
