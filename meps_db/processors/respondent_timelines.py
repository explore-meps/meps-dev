from meps_db.processors.encoders.population_characteristics_encoder import PopulationCharacteristicsEncoder
from meps_db.processors.encoders.office_based_visits_encoder import OfficeBasedVisitsEncoder
from meps_db.processors.encoders.outpatient_visits_encoder import OutpatientVisitsEncoder
from meps_db.processors.encoders.emergency_room_event_encoder import EmergencyRoomVisitsEncoder
from meps_db.processors.encoders.hosptial_inpatient_stays_encoder import HospitalInpatientStaysEncoder
from meps_db.processors.encoders.dental_care_events_encoder import DentalVisitsEncoder
from meps_db.processors.encoders.home_health_days_encoder import HomeHealthEncoder
from meps_db.processors.encoders.other_medical_events_encoder import OtherMedicalExpensesEncoder
from meps_db.processors.encoders.prescribed_medicines_encoder import PrescribedMedicinesEncoder


class RespondentHistoryGenerator:
    """ Queries the Events Tables and merges events from various sources to respondents.  """

    def __init__(self, years, dupersids=None):
        """
            Required_Inputs:
                years: Years to fetch data for
            Optional Inputs:
                dupersids: list of respondent dupersids to exclusively fetch data for
        """

        self.years=years
        self.dupersids=dupersids

    def run(self):
        """ Primary Entry Point of RespondentHistoryGenerator """

        respondent_history = {}

        for year in self.years:
            population = PopulationCharacteristicsEncoder(year=year, dupersids=self.dupersids).run()
            office_based = OfficeBasedVisitsEncoder(year=year, dupersids=self.dupersids).run() 
            outpatient = OutpatientVisitsEncoder(year=year, dupersids=self.dupersids).run() 
            emergency_room = EmergencyRoomVisitsEncoder(year=year, dupersids=self.dupersids).run()
            hosptial_inpatient = HospitalInpatientStaysEncoder(year=year, dupersids=self.dupersids).run()
            dental_care = DentalVisitsEncoder(year=year, dupersids=self.dupersids).run()
            home_health = HomeHealthEncoder(year=year, dupersids=self.dupersids).run()
            other_medical = OtherMedicalExpensesEncoder(year=year, dupersids=self.dupersids).run()
            presciption_medicines = PrescribedMedicinesEncoder(year=year, dupersids=self.dupersids).run()

            respondent_history[year] = self.merge_sources(
                population=population,
                office_based=office_based,
                outpatient=outpatient,
                emergency_room=emergency_room,
                hosptial_inpatient=hosptial_inpatient,
                dental_care=dental_care,
                home_health=home_health,
                other_medical=other_medical,
                presciption_medicines=presciption_medicines,
            )
        
        return respondent_history

    @staticmethod
    def merge_sources(
        population,
        office_based,
        outpatient,
        emergency_room,
        hosptial_inpatient,
        dental_care,
        home_health,
        other_medical,
        presciption_medicines,
    ):
        """ Takes a population dictionary and dictionaries of all events types. Matches events to each member of the
        population dictionary. """

        event_lookup = [
            ("office_based", office_based),
            ("outpatient", outpatient),
            ("emergency_room", emergency_room),
            ("hosptial_inpatient", hosptial_inpatient),
            ("dental_care", dental_care),
            ("home_health", home_health),
            ("other_medical", other_medical),
            ("presciption_medicines", presciption_medicines),
        ]

        for resp_id, resp_dict in population.items():
            for event_name, event_dict in event_lookup:
                resp_dict.update(
                    {
                        event_name: event_dict.get(resp_id, [])
                    }
                )
        
        return population
