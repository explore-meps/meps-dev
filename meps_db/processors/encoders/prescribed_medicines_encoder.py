from meps_db.components.models.prescribed_medicines_models import (
    PrescribedMedicines18,
    PrescribedMedicines17,
    PrescribedMedicines16,
    PrescribedMedicines15,
    PrescribedMedicines14,
    PrescribedMedicines13,
    PrescribedMedicines12,
    PrescribedMedicines11,
    PrescribedMedicines10,
    PrescribedMedicines09,
    PrescribedMedicines08,
    PrescribedMedicines07,
    PrescribedMedicines06,
    PrescribedMedicines05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder


class PrescribedMedicinesEncoder(BaseEncoder):
    """  Queries the  PrescribedMedicines Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year = year
        self.dupersids = dupersids

        self.PM_LOOKUPS = {
            2018: {"model": PrescribedMedicines18, "fields": {"DUPERSID", "RXRECIDX"},},
            2017: {"model": PrescribedMedicines17, "fields": {"DUPERSID", "RXRECIDX"},},
            2016: {"model": PrescribedMedicines16, "fields": {"DUPERSID", "RXRECIDX"},},
            2015: {"model": PrescribedMedicines15, "fields": {"DUPERSID", "RXRECIDX"},},
            2014: {"model": PrescribedMedicines14, "fields": {"DUPERSID", "RXRECIDX"},},
            2013: {"model": PrescribedMedicines13, "fields": {"DUPERSID", "RXRECIDX"},},
            2012: {"model": PrescribedMedicines12, "fields": {"DUPERSID", "RXRECIDX"},},
            2011: {"model": PrescribedMedicines11, "fields": {"DUPERSID", "RXRECIDX"},},
            2010: {"model": PrescribedMedicines10, "fields": {"DUPERSID", "RXRECIDX"},},
            2009: {"model": PrescribedMedicines09, "fields": {"DUPERSID", "RXRECIDX"},},
            2008: {"model": PrescribedMedicines08, "fields": {"DUPERSID", "RXRECIDX"},},
            2007: {"model": PrescribedMedicines07, "fields": {"DUPERSID", "RXRECIDX"},},
            2006: {"model": PrescribedMedicines06, "fields": {"DUPERSID", "RXRECIDX"},},
            2005: {"model": PrescribedMedicines05, "fields": {"DUPERSID", "RXRECIDX"},},
        }

    def run(self):
        """ Groups events by respondents. """

        if self.dupersids:
            events = list(
                self.PM_LOOKUPS[self.year]["model"]
                .objects.filter(DUPERSID__in=self.dupersids)
                .values(*self.PM_LOOKUPS[self.year]["fields"])
            )
        else:
            events = list(
                self.PM_LOOKUPS[self.year]["model"].objects.all().values(*self.PM_LOOKUPS[self.year]["fields"])
            )

        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {"unique_rx": event["RXRECIDX"],}
            )

        return respondents
