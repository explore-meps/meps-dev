from meps_db.components.models.dental_visits_models import (
    DentalVisits18,
    DentalVisits17,
    DentalVisits16,
    DentalVisits15,
    DentalVisits14,
    DentalVisits13,
    DentalVisits12,
    DentalVisits11,
    DentalVisits10,
    DentalVisits09,
    DentalVisits08,
    DentalVisits07,
    DentalVisits06,
    DentalVisits05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class DentalVisitsEncoder(BaseEncoder):
    """  Queries the DentalVisits Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.DV_LOOKUPS = {
            2018: {"model": DentalVisits18, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2017: {"model": DentalVisits17, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2016: {"model": DentalVisits16, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2015: {"model": DentalVisits15, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2014: {"model": DentalVisits14, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2013: {"model": DentalVisits13, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2012: {"model": DentalVisits12, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2011: {"model": DentalVisits11, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2010: {"model": DentalVisits10, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2009: {"model": DentalVisits09, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2008: {"model": DentalVisits08, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2007: {"model": DentalVisits07, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2006: {"model": DentalVisits06, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
            2005: {"model": DentalVisits05, "fields": {"DUPERSID", "EVNTIDX", "DVDATEYR", "DVDATEMM"},},
        }

    def run(self):
        """ Groups events by respondents. Return a list of ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.DV_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.DV_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.DV_LOOKUPS[self.year]["model"].objects.all().values(*self.DV_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["DVDATEYR"], month_str=event["DVDATEMM"]),
                }
            )

        respondents = self.order_histories(respondents=respondents)

        return respondents
