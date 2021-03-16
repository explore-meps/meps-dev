from meps_db.components.models.other_medical_expenses_models import (
    OtherMedicalExpenses18,
    OtherMedicalExpenses17,
    OtherMedicalExpenses16,
    OtherMedicalExpenses15,
    OtherMedicalExpenses14,
    OtherMedicalExpenses13,
    OtherMedicalExpenses12,
    OtherMedicalExpenses11,
    OtherMedicalExpenses10,
    OtherMedicalExpenses09,
    OtherMedicalExpenses08,
    OtherMedicalExpenses07,
    OtherMedicalExpenses06,
    OtherMedicalExpenses05,
)
from meps_db.processors.encoders.base_encoder import BaseEncoder

class OtherMedicalExpensesEncoder(BaseEncoder):
    """  Queries the OtherMedicalExpenses Tables. Encodes fields from strings to usable data types. """

    def __init__(self, year, dupersids=None):
        """
            Required_Inputs:
                year: Year to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.year=year
        self.dupersids=dupersids

        self.OM_LOOKUPS = {
            2018: {
                "model": OtherMedicalExpenses18,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2017: {
                "model": OtherMedicalExpenses17,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2016: {
                "model": OtherMedicalExpenses16,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2015: {
                "model": OtherMedicalExpenses15,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2014: {
                "model": OtherMedicalExpenses14,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2013: {
                "model": OtherMedicalExpenses13,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2012: {
                "model": OtherMedicalExpenses12,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2011: {
                "model": OtherMedicalExpenses11,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2010: {
                "model": OtherMedicalExpenses10,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2009: {
                "model": OtherMedicalExpenses09,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2008: {
                "model": OtherMedicalExpenses08,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2007: {
                "model": OtherMedicalExpenses07,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2006: {
                "model": OtherMedicalExpenses06,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
            2005: {
                "model": OtherMedicalExpenses05,
                "fields": {"DUPERSID",  "EVNTIDX"},
            },
        }

    def run(self):
        """ Groups events by respondents. Return a list of ordered events for each respondent. """

        if self.dupersids:
            events = list(
                self.OM_LOOKUPS[self.year]["model"].objects.filter(
                    DUPERSID__in=self.dupersids).values(*self.OM_LOOKUPS[self.year]["fields"]
                )
            )
        else:
            events = list(
                self.OM_LOOKUPS[self.year]["model"].objects.all().values(*self.OM_LOOKUPS[self.year]["fields"])
            )
            
        respondents = {}
        for event in events:
            resp_id = event["DUPERSID"]
            if resp_id not in respondents:
                respondents[resp_id] = []
            respondents[resp_id].append(
                {
                    "event_id": event["EVNTIDX"],
                }
            )
        
        return respondents
