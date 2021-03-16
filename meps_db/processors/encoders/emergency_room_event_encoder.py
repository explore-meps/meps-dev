from meps_db.components.models.emergency_room_visits_models import (
    EmergencyRoomVisits18,
    EmergencyRoomVisits17,
    EmergencyRoomVisits16,
    EmergencyRoomVisits15,
    EmergencyRoomVisits14,
    EmergencyRoomVisits13,
    EmergencyRoomVisits12,
    EmergencyRoomVisits11,
    EmergencyRoomVisits10,
    EmergencyRoomVisits09,
    EmergencyRoomVisits08,
    EmergencyRoomVisits07,
    EmergencyRoomVisits06,
    EmergencyRoomVisits05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class EmergencyRoomVisitsEncoder(BaseEncoder):
    """  Queries the EmergencyRoomVisits Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.ER_LOOKUPS = {
            2018: {"model": EmergencyRoomVisits18, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2017: {"model": EmergencyRoomVisits17, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2016: {"model": EmergencyRoomVisits16, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2015: {"model": EmergencyRoomVisits15, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2014: {"model": EmergencyRoomVisits14, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2013: {"model": EmergencyRoomVisits13, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2012: {"model": EmergencyRoomVisits12, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2011: {"model": EmergencyRoomVisits11, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2010: {"model": EmergencyRoomVisits10, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2009: {"model": EmergencyRoomVisits09, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2008: {"model": EmergencyRoomVisits08, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2007: {"model": EmergencyRoomVisits07, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2006: {"model": EmergencyRoomVisits06, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
            2005: {"model": EmergencyRoomVisits05, "fields": {"DUPERSID", "EVNTIDX", "ERDATEYR", "ERDATEMM"},},
        }

    def run(self):
        """ Groups events by respondents. Return a list of ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.ER_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.ER_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.ER_LOOKUPS[self.year]["model"].objects.all().values(*self.ER_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["ERDATEYR"], month_str=event["ERDATEMM"]),
                }
            )

        respondents = self.order_histories(respondents=respondents)

        return respondents
