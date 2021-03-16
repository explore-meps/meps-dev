from meps_db.components.models.hospital_inpatient_stays_models import (
    HospitalInpatientStays18,
    HospitalInpatientStays17,
    HospitalInpatientStays16,
    HospitalInpatientStays15,
    HospitalInpatientStays14,
    HospitalInpatientStays13,
    HospitalInpatientStays12,
    HospitalInpatientStays11,
    HospitalInpatientStays10,
    HospitalInpatientStays09,
    HospitalInpatientStays08,
    HospitalInpatientStays07,
    HospitalInpatientStays06,
    HospitalInpatientStays05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class HospitalInpatientStaysEncoder(BaseEncoder):
    """  Queries the HospitalInpatientStays Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.HIS_LOOKUPS = {
            2018: {
                "model": HospitalInpatientStays18,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2017: {
                "model": HospitalInpatientStays17,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2016: {
                "model": HospitalInpatientStays16,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2015: {
                "model": HospitalInpatientStays15,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2014: {
                "model": HospitalInpatientStays14,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2013: {
                "model": HospitalInpatientStays13,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2012: {
                "model": HospitalInpatientStays12,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2011: {
                "model": HospitalInpatientStays11,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2010: {
                "model": HospitalInpatientStays10,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2009: {
                "model": HospitalInpatientStays09,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2008: {
                "model": HospitalInpatientStays08,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2007: {
                "model": HospitalInpatientStays07,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2006: {
                "model": HospitalInpatientStays06,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
            2005: {
                "model": HospitalInpatientStays05,
                "fields": {"DUPERSID", "EVNTIDX", "IPBEGYR", "IPBEGMM", "NUMNIGHX"},
            },
        }

    def run(self):
        """ Groups events by respondents. Stores the number of nights spent in hospital. Return a list of ordered 
        events for each respondent. """

        if self.dupersids:
            events = list(
                self.HIS_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.HIS_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.HIS_LOOKUPS[self.year]["model"].objects.all().values(*self.HIS_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                    "date": self.generate_date(year_str=event["IPBEGYR"], month_str=event["IPBEGMM"]),
                    "nights": int(event["NUMNIGHX"]),
                }
            )

        respondents = self.order_histories(respondents=respondents)

        return respondents
