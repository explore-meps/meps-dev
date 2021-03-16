from meps_db.components.models.home_health_models import (
    HomeHealth18,
    HomeHealth17,
    HomeHealth16,
    HomeHealth15,
    HomeHealth14,
    HomeHealth13,
    HomeHealth12,
    HomeHealth11,
    HomeHealth10,
    HomeHealth09,
    HomeHealth08,
    HomeHealth07,
    HomeHealth06,
    HomeHealth05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class HomeHealthEncoder(BaseEncoder):
    """  Queries the HomeHealth Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.HH_LOOKUPS = {
            2018: {
                "model": HomeHealth18,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2017: {
                "model": HomeHealth17,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2016: {
                "model": HomeHealth16,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2015: {
                "model": HomeHealth15,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2014: {
                "model": HomeHealth14,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2013: {
                "model": HomeHealth13,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2012: {
                "model": HomeHealth12,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2011: {
                "model": HomeHealth11,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2010: {
                "model": HomeHealth10,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2009: {
                "model": HomeHealth09,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2008: {
                "model": HomeHealth08,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2007: {
                "model": HomeHealth07,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2006: {
                "model": HomeHealth06,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
            2005: {
                "model": HomeHealth05,
                "fields": {"DUPERSID", "EVNTIDX", "HHDATEYR", "HHDATEMM", "MPCELIG", "HHDAYS"},
            },
        }

    def run(self):
        """ Groups events by respondents. Return a list of ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.HH_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.HH_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.HH_LOOKUPS[self.year]["model"].objects.all().values(*self.HH_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []

            # overall count
            home_health_provider_days = 0
            if event["HHDAYS"] not in {"-15", "-9", "-8", "-7"}:
                home_health_provider_days = int(event["HHDAYS"])
            else:
                home_health_provider_days = None

            # classify source
            home_health_agency_days, home_health_non_agency_days, home_health_informal_days = 0, 0, 0
            if event["MPCELIG"] == "1":
                if event["HHDAYS"] not in {"-15", "-9", "-8", "-7"}:
                    home_health_agency_days = int(event["HHDAYS"])
                else:
                    home_health_agency_days = None

            if event["MPCELIG"] == "2":
                if event["HHDAYS"] not in {"-15", "-9", "-8", "-7"}:
                    home_health_non_agency_days = int(event["HHDAYS"])
                else:
                    home_health_non_agency_days = None

            if event["MPCELIG"] == "3":
                if event["HHDAYS"] not in {"-15", "-9", "-8", "-7"}:
                    home_health_informal_days = int(event["HHDAYS"])
                else:
                    home_health_informal_days = None

            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["HHDATEYR"], month_str=event["HHDATEMM"]),
                    "home_health_provider_days": home_health_provider_days,
                    "home_health_agency_days": home_health_agency_days,
                    "home_health_non_agency_days": home_health_non_agency_days,
                    "home_health_informal_days": home_health_informal_days,
                }
            )

        respondents = self.order_histories(respondents=respondents)

        return respondents
