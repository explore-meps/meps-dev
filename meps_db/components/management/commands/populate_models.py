from django.core.management.base import BaseCommand

from meps_db.components.populators import ComponentPopulator
from meps_db.components.reference import DATA_FILES_YEARS, BASE_MODELS

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

from meps_db.components.models.medical_conditions_models import (
    MedicalConditions18,
    MedicalConditions17,
    MedicalConditions16,
    MedicalConditions15,
    MedicalConditions14,
    MedicalConditions13,
    MedicalConditions12,
    MedicalConditions11,
    MedicalConditions10,
    MedicalConditions09,
    MedicalConditions08,
    MedicalConditions07,
    MedicalConditions06,
    MedicalConditions05,
)

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

from meps_db.components.models.population_characteristics_models import (
    PopulationCharacteristics18,
    PopulationCharacteristics17,
    PopulationCharacteristics16,
    PopulationCharacteristics15,
    PopulationCharacteristics14,
    PopulationCharacteristics13,
    PopulationCharacteristics12,
    PopulationCharacteristics11,
    PopulationCharacteristics10,
    PopulationCharacteristics09,
    PopulationCharacteristics08,
    PopulationCharacteristics07,
    PopulationCharacteristics06,
    PopulationCharacteristics05,
)

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


class Command(BaseCommand):
    """ Management command to populate components models. Run in terminal.
        ex:
            python manage.py populate_components
            python manage.py populate_components --years "2016" "2017" --models "PrescribedMedicines"
    """

    help = "Populates the component models"

    def add_arguments(self, parser):
        parser.add_argument(
            "--years", nargs="*", type=int, help="declare year to populate models with like '2016'",
        )
        parser.add_argument(
            "--models", nargs="*", help="declare specific table to populate with like 'PrescribedMedicines'",
        )

    def handle(self, *args, **options):

        model_params_dict = {
            "DentalVisits": {
                "populator": ComponentPopulator,
                "data_type": "dental_visits",
                "object_name": "DentalVisits",
            },
            "EmergencyRoomVisits": {
                "populator": ComponentPopulator,
                "data_type": "emergency_room_visits",
                "object_name": "EmergencyRoomVisits",
            },
            "HomeHealth": {"populator": ComponentPopulator, "data_type": "home_health", "object_name": "HomeHealth"},
            "HospitalInpatientStays": {
                "populator": ComponentPopulator,
                "data_type": "hospital_inpatient_stays",
                "object_name": "HospitalInpatientStays",
            },
            "MedicalConditions": {
                "populator": ComponentPopulator,
                "data_type": "medical_conditions",
                "object_name": "MedicalConditions",
            },
            "OfficeBasedVisits": {
                "populator": ComponentPopulator,
                "data_type": "office_based_visits",
                "object_name": "OfficeBasedVisits",
            },
            "OtherMedicalExpenses": {
                "populator": ComponentPopulator,
                "data_type": "other_medical_expenses",
                "object_name": "OtherMedicalExpenses",
            },
            "OutpatientVisits": {
                "populator": ComponentPopulator,
                "data_type": "outpatient_visits",
                "object_name": "OutpatientVisits",
            },
            "PopulationCharacteristics": {
                "populator": ComponentPopulator,
                "data_type": "population_characteristics",
                "object_name": "PopulationCharacteristics",
            },
            "PrescribedMedicines": {
                "populator": ComponentPopulator,
                "data_type": "prescribed_medicines",
                "object_name": "PrescribedMedicines",
            },
        }

        if options["years"] is None:
            years = DATA_FILES_YEARS
        else:
            years = options["years"]

        if options["models"] is None:
            model_list = BASE_MODELS
        else:
            model_list = [model for model in options["models"] if model in BASE_MODELS]

        self.populate(
            years=years, model_list=model_list, model_params_dict=model_params_dict, options=options,
        )

    def populate(self, years, model_list, model_params_dict, options):
        """ Takes a list of year, a list of models and a reference dictionary associated with each model. Populates
        the all models within the list of years """

        MODEL_LOOKUP = {
            "DentalVisits": {
                2018: DentalVisits18,
                2017: DentalVisits17,
                2016: DentalVisits16,
                2015: DentalVisits15,
                2014: DentalVisits14,
                2013: DentalVisits13,
                2012: DentalVisits12,
                2011: DentalVisits11,
                2010: DentalVisits10,
                2009: DentalVisits09,
                2008: DentalVisits08,
                2007: DentalVisits07,
                2006: DentalVisits06,
                2005: DentalVisits05,
            },
            "EmergencyRoomVisits": {
                2018: EmergencyRoomVisits18,
                2017: EmergencyRoomVisits17,
                2016: EmergencyRoomVisits16,
                2015: EmergencyRoomVisits15,
                2014: EmergencyRoomVisits14,
                2013: EmergencyRoomVisits13,
                2012: EmergencyRoomVisits12,
                2011: EmergencyRoomVisits11,
                2010: EmergencyRoomVisits10,
                2009: EmergencyRoomVisits09,
                2008: EmergencyRoomVisits08,
                2007: EmergencyRoomVisits07,
                2006: EmergencyRoomVisits06,
                2005: EmergencyRoomVisits05,
            },
            "HomeHealth": {
                2018: HomeHealth18,
                2017: HomeHealth17,
                2016: HomeHealth16,
                2015: HomeHealth15,
                2014: HomeHealth14,
                2013: HomeHealth13,
                2012: HomeHealth12,
                2011: HomeHealth11,
                2010: HomeHealth10,
                2009: HomeHealth09,
                2008: HomeHealth08,
                2007: HomeHealth07,
                2006: HomeHealth06,
                2005: HomeHealth05,
            },
            "HospitalInpatientStays": {
                2018: HospitalInpatientStays18,
                2017: HospitalInpatientStays17,
                2016: HospitalInpatientStays16,
                2015: HospitalInpatientStays15,
                2014: HospitalInpatientStays14,
                2013: HospitalInpatientStays13,
                2012: HospitalInpatientStays12,
                2011: HospitalInpatientStays11,
                2010: HospitalInpatientStays10,
                2009: HospitalInpatientStays09,
                2008: HospitalInpatientStays08,
                2007: HospitalInpatientStays07,
                2006: HospitalInpatientStays06,
                2005: HospitalInpatientStays05,
            },
            "MedicalConditions": {
                2018: MedicalConditions18,
                2017: MedicalConditions17,
                2016: MedicalConditions16,
                2015: MedicalConditions15,
                2014: MedicalConditions14,
                2013: MedicalConditions13,
                2012: MedicalConditions12,
                2011: MedicalConditions11,
                2010: MedicalConditions10,
                2009: MedicalConditions09,
                2008: MedicalConditions08,
                2007: MedicalConditions07,
                2006: MedicalConditions06,
                2005: MedicalConditions05,
            },
            "OfficeBasedVisits": {
                2018: OfficeBasedVisits18,
                2017: OfficeBasedVisits17,
                2016: OfficeBasedVisits16,
                2015: OfficeBasedVisits15,
                2014: OfficeBasedVisits14,
                2013: OfficeBasedVisits13,
                2012: OfficeBasedVisits12,
                2011: OfficeBasedVisits11,
                2010: OfficeBasedVisits10,
                2009: OfficeBasedVisits09,
                2008: OfficeBasedVisits08,
                2007: OfficeBasedVisits07,
                2006: OfficeBasedVisits06,
                2005: OfficeBasedVisits05,
            },
            "OtherMedicalExpenses": {
                2018: OtherMedicalExpenses18,
                2017: OtherMedicalExpenses17,
                2016: OtherMedicalExpenses16,
                2015: OtherMedicalExpenses15,
                2014: OtherMedicalExpenses14,
                2013: OtherMedicalExpenses13,
                2012: OtherMedicalExpenses12,
                2011: OtherMedicalExpenses11,
                2010: OtherMedicalExpenses10,
                2009: OtherMedicalExpenses09,
                2008: OtherMedicalExpenses08,
                2007: OtherMedicalExpenses07,
                2006: OtherMedicalExpenses06,
                2005: OtherMedicalExpenses05,
            },
            "OutpatientVisits": {
                2018: OutpatientVisits18,
                2017: OutpatientVisits17,
                2016: OutpatientVisits16,
                2015: OutpatientVisits15,
                2014: OutpatientVisits14,
                2013: OutpatientVisits13,
                2012: OutpatientVisits12,
                2011: OutpatientVisits11,
                2010: OutpatientVisits10,
                2009: OutpatientVisits09,
                2008: OutpatientVisits08,
                2007: OutpatientVisits07,
                2006: OutpatientVisits06,
                2005: OutpatientVisits05,
            },
            "PopulationCharacteristics": {
                2018: PopulationCharacteristics18,
                2017: PopulationCharacteristics17,
                2016: PopulationCharacteristics16,
                2015: PopulationCharacteristics15,
                2014: PopulationCharacteristics14,
                2013: PopulationCharacteristics13,
                2012: PopulationCharacteristics12,
                2011: PopulationCharacteristics11,
                2010: PopulationCharacteristics10,
                2009: PopulationCharacteristics09,
                2008: PopulationCharacteristics08,
                2007: PopulationCharacteristics07,
                2006: PopulationCharacteristics06,
                2005: PopulationCharacteristics05,
            },
            "PrescribedMedicines": {
                2018: PrescribedMedicines18,
                2017: PrescribedMedicines17,
                2016: PrescribedMedicines16,
                2015: PrescribedMedicines15,
                2014: PrescribedMedicines14,
                2013: PrescribedMedicines13,
                2012: PrescribedMedicines12,
                2011: PrescribedMedicines11,
                2010: PrescribedMedicines10,
                2009: PrescribedMedicines09,
                2008: PrescribedMedicines08,
                2007: PrescribedMedicines07,
                2006: PrescribedMedicines06,
                2005: PrescribedMedicines05,
            },
        }

        for year in years:
            for model_key in model_list:
                populator_class = model_params_dict[model_key]["populator"](
                    year=year, data_type=model_params_dict[model_key]["data_type"]
                )
                obj_list = populator_class.run()

                # look up model based on model key and year
                model = MODEL_LOOKUP[model_key][year]

                model_objs = [model(**obj) for obj in obj_list]
                model.objects.bulk_create(model_objs)

                if options["verbosity"] > 0:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully populated {model_params_dict[model_key]['object_name']} Model with "
                            f"{len(model_objs) :,} entries from year {year}"
                        )
                    )
