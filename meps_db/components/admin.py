from django.contrib import admin

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

from meps_db.components.models.full_year_consolidated_models import (
    FullYearConsolidated18,
    FullYearConsolidated17,
    FullYearConsolidated16,
    FullYearConsolidated15,
    FullYearConsolidated14,
    FullYearConsolidated13,
    FullYearConsolidated12,
    FullYearConsolidated11,
    FullYearConsolidated10,
    FullYearConsolidated09,
    FullYearConsolidated08,
    FullYearConsolidated07,
    FullYearConsolidated06,
    FullYearConsolidated05,
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


class AdminFullYearConsolidated18(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated17(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated16(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated15(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated14(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated13(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated12(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated11(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated10(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated09(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated08(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated07(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated06(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminFullYearConsolidated05(admin.ModelAdmin):
    """ Admin settings for FullYearConsolidated05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = FullYearConsolidated05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics18(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics17(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics16(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics15(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics14(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics13(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics12(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics11(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics10(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics09(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics08(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics07(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics06(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPopulationCharacteristics05(admin.ModelAdmin):
    """ Admin settings for PopulationCharacteristics05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PopulationCharacteristics05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions18(admin.ModelAdmin):
    """ Admin settings for MedicalConditions18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions17(admin.ModelAdmin):
    """ Admin settings for MedicalConditions17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions16(admin.ModelAdmin):
    """ Admin settings for MedicalConditions16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions15(admin.ModelAdmin):
    """ Admin settings for MedicalConditions15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions14(admin.ModelAdmin):
    """ Admin settings for MedicalConditions14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions13(admin.ModelAdmin):
    """ Admin settings for MedicalConditions13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions12(admin.ModelAdmin):
    """ Admin settings for MedicalConditions12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions11(admin.ModelAdmin):
    """ Admin settings for MedicalConditions11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions10(admin.ModelAdmin):
    """ Admin settings for MedicalConditions10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions09(admin.ModelAdmin):
    """ Admin settings for MedicalConditions09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions08(admin.ModelAdmin):
    """ Admin settings for MedicalConditions08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions07(admin.ModelAdmin):
    """ Admin settings for MedicalConditions07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions06(admin.ModelAdmin):
    """ Admin settings for MedicalConditions06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminMedicalConditions05(admin.ModelAdmin):
    """ Admin settings for MedicalConditions05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = MedicalConditions05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines18(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines17(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines16(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines15(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines14(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines13(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines12(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines11(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines10(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines09(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines08(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines07(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines06(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminPrescribedMedicines05(admin.ModelAdmin):
    """ Admin settings for PrescribedMedicines05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = PrescribedMedicines05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits18(admin.ModelAdmin):
    """ Admin settings for DentalVisits18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits17(admin.ModelAdmin):
    """ Admin settings for DentalVisits17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits16(admin.ModelAdmin):
    """ Admin settings for DentalVisits16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits15(admin.ModelAdmin):
    """ Admin settings for DentalVisits15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits14(admin.ModelAdmin):
    """ Admin settings for DentalVisits14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits13(admin.ModelAdmin):
    """ Admin settings for DentalVisits13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits12(admin.ModelAdmin):
    """ Admin settings for DentalVisits12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits11(admin.ModelAdmin):
    """ Admin settings for DentalVisits11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits10(admin.ModelAdmin):
    """ Admin settings for DentalVisits10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits09(admin.ModelAdmin):
    """ Admin settings for DentalVisits09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits08(admin.ModelAdmin):
    """ Admin settings for DentalVisits08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits07(admin.ModelAdmin):
    """ Admin settings for DentalVisits07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits06(admin.ModelAdmin):
    """ Admin settings for DentalVisits06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminDentalVisits05(admin.ModelAdmin):
    """ Admin settings for DentalVisits05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = DentalVisits05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses18(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses17(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses16(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses15(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses14(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses13(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses12(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses11(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses10(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses09(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses08(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses07(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses06(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOtherMedicalExpenses05(admin.ModelAdmin):
    """ Admin settings for OtherMedicalExpenses05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OtherMedicalExpenses05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays18(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays17(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays16(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays15(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays14(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays13(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays12(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays11(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays10(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays09(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays08(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays07(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays06(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHospitalInpatientStays05(admin.ModelAdmin):
    """ Admin settings for HospitalInpatientStays05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HospitalInpatientStays05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits18(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits17(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits16(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits15(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits14(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits13(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits12(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits11(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits10(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits09(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits08(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits07(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits06(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminEmergencyRoomVisits05(admin.ModelAdmin):
    """ Admin settings for EmergencyRoomVisits05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = EmergencyRoomVisits05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits18(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits17(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits16(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits15(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits14(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits13(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits12(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits11(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits10(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits09(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits08(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits07(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits06(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOutpatientVisits05(admin.ModelAdmin):
    """ Admin settings for OutpatientVisits05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OutpatientVisits05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits18(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits17(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits16(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits15(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits14(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits13(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits12(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits11(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits10(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits09(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits08(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits07(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits06(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminOfficeBasedVisits05(admin.ModelAdmin):
    """ Admin settings for OfficeBasedVisits05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = OfficeBasedVisits05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth18(admin.ModelAdmin):
    """ Admin settings for HomeHealth18 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth18

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth17(admin.ModelAdmin):
    """ Admin settings for HomeHealth17 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth17

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth16(admin.ModelAdmin):
    """ Admin settings for HomeHealth16 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth16

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth15(admin.ModelAdmin):
    """ Admin settings for HomeHealth15 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth15

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth14(admin.ModelAdmin):
    """ Admin settings for HomeHealth14 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth14

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth13(admin.ModelAdmin):
    """ Admin settings for HomeHealth13 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth13

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth12(admin.ModelAdmin):
    """ Admin settings for HomeHealth12 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth12

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth11(admin.ModelAdmin):
    """ Admin settings for HomeHealth11 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth11

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth10(admin.ModelAdmin):
    """ Admin settings for HomeHealth10 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth10

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth09(admin.ModelAdmin):
    """ Admin settings for HomeHealth09 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth09

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth08(admin.ModelAdmin):
    """ Admin settings for HomeHealth08 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth08

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth07(admin.ModelAdmin):
    """ Admin settings for HomeHealth07 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth07

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth06(admin.ModelAdmin):
    """ Admin settings for HomeHealth06 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth06

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


class AdminHomeHealth05(admin.ModelAdmin):
    """ Admin settings for HomeHealth05 model"""

    def has_change_permission(self, request, obj=None):
        """ Do not allow users to edit model instances """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Do not allow users to delete model instances """
        return False

    model = HomeHealth05

    # Column names to display on table
    field_names = [field.name for field in model._meta.get_fields()]
    list_display = field_names

    # Navigation
    search_fields = ["DUPERSID"]
    list_per_page = 15


admin.site.register(FullYearConsolidated18, AdminFullYearConsolidated18)
admin.site.register(FullYearConsolidated17, AdminFullYearConsolidated17)
admin.site.register(FullYearConsolidated16, AdminFullYearConsolidated16)
admin.site.register(FullYearConsolidated15, AdminFullYearConsolidated15)
admin.site.register(FullYearConsolidated14, AdminFullYearConsolidated14)
admin.site.register(FullYearConsolidated13, AdminFullYearConsolidated13)
admin.site.register(FullYearConsolidated12, AdminFullYearConsolidated12)
admin.site.register(FullYearConsolidated11, AdminFullYearConsolidated11)
admin.site.register(FullYearConsolidated10, AdminFullYearConsolidated10)
admin.site.register(FullYearConsolidated09, AdminFullYearConsolidated09)
admin.site.register(FullYearConsolidated08, AdminFullYearConsolidated08)
admin.site.register(FullYearConsolidated07, AdminFullYearConsolidated07)
admin.site.register(FullYearConsolidated06, AdminFullYearConsolidated06)
admin.site.register(FullYearConsolidated05, AdminFullYearConsolidated05)
admin.site.register(PopulationCharacteristics18, AdminPopulationCharacteristics18)
admin.site.register(PopulationCharacteristics17, AdminPopulationCharacteristics17)
admin.site.register(PopulationCharacteristics16, AdminPopulationCharacteristics16)
admin.site.register(PopulationCharacteristics15, AdminPopulationCharacteristics15)
admin.site.register(PopulationCharacteristics14, AdminPopulationCharacteristics14)
admin.site.register(PopulationCharacteristics13, AdminPopulationCharacteristics13)
admin.site.register(PopulationCharacteristics12, AdminPopulationCharacteristics12)
admin.site.register(PopulationCharacteristics11, AdminPopulationCharacteristics11)
admin.site.register(PopulationCharacteristics10, AdminPopulationCharacteristics10)
admin.site.register(PopulationCharacteristics09, AdminPopulationCharacteristics09)
admin.site.register(PopulationCharacteristics08, AdminPopulationCharacteristics08)
admin.site.register(PopulationCharacteristics07, AdminPopulationCharacteristics07)
admin.site.register(PopulationCharacteristics06, AdminPopulationCharacteristics06)
admin.site.register(PopulationCharacteristics05, AdminPopulationCharacteristics05)
admin.site.register(MedicalConditions18, AdminMedicalConditions18)
admin.site.register(MedicalConditions17, AdminMedicalConditions17)
admin.site.register(MedicalConditions16, AdminMedicalConditions16)
admin.site.register(MedicalConditions15, AdminMedicalConditions15)
admin.site.register(MedicalConditions14, AdminMedicalConditions14)
admin.site.register(MedicalConditions13, AdminMedicalConditions13)
admin.site.register(MedicalConditions12, AdminMedicalConditions12)
admin.site.register(MedicalConditions11, AdminMedicalConditions11)
admin.site.register(MedicalConditions10, AdminMedicalConditions10)
admin.site.register(MedicalConditions09, AdminMedicalConditions09)
admin.site.register(MedicalConditions08, AdminMedicalConditions08)
admin.site.register(MedicalConditions07, AdminMedicalConditions07)
admin.site.register(MedicalConditions06, AdminMedicalConditions06)
admin.site.register(MedicalConditions05, AdminMedicalConditions05)
admin.site.register(PrescribedMedicines18, AdminPrescribedMedicines18)
admin.site.register(PrescribedMedicines17, AdminPrescribedMedicines17)
admin.site.register(PrescribedMedicines16, AdminPrescribedMedicines16)
admin.site.register(PrescribedMedicines15, AdminPrescribedMedicines15)
admin.site.register(PrescribedMedicines14, AdminPrescribedMedicines14)
admin.site.register(PrescribedMedicines13, AdminPrescribedMedicines13)
admin.site.register(PrescribedMedicines12, AdminPrescribedMedicines12)
admin.site.register(PrescribedMedicines11, AdminPrescribedMedicines11)
admin.site.register(PrescribedMedicines10, AdminPrescribedMedicines10)
admin.site.register(PrescribedMedicines09, AdminPrescribedMedicines09)
admin.site.register(PrescribedMedicines08, AdminPrescribedMedicines08)
admin.site.register(PrescribedMedicines07, AdminPrescribedMedicines07)
admin.site.register(PrescribedMedicines06, AdminPrescribedMedicines06)
admin.site.register(PrescribedMedicines05, AdminPrescribedMedicines05)
admin.site.register(DentalVisits18, AdminDentalVisits18)
admin.site.register(DentalVisits17, AdminDentalVisits17)
admin.site.register(DentalVisits16, AdminDentalVisits16)
admin.site.register(DentalVisits15, AdminDentalVisits15)
admin.site.register(DentalVisits14, AdminDentalVisits14)
admin.site.register(DentalVisits13, AdminDentalVisits13)
admin.site.register(DentalVisits12, AdminDentalVisits12)
admin.site.register(DentalVisits11, AdminDentalVisits11)
admin.site.register(DentalVisits10, AdminDentalVisits10)
admin.site.register(DentalVisits09, AdminDentalVisits09)
admin.site.register(DentalVisits08, AdminDentalVisits08)
admin.site.register(DentalVisits07, AdminDentalVisits07)
admin.site.register(DentalVisits06, AdminDentalVisits06)
admin.site.register(DentalVisits05, AdminDentalVisits05)
admin.site.register(OtherMedicalExpenses18, AdminOtherMedicalExpenses18)
admin.site.register(OtherMedicalExpenses17, AdminOtherMedicalExpenses17)
admin.site.register(OtherMedicalExpenses16, AdminOtherMedicalExpenses16)
admin.site.register(OtherMedicalExpenses15, AdminOtherMedicalExpenses15)
admin.site.register(OtherMedicalExpenses14, AdminOtherMedicalExpenses14)
admin.site.register(OtherMedicalExpenses13, AdminOtherMedicalExpenses13)
admin.site.register(OtherMedicalExpenses12, AdminOtherMedicalExpenses12)
admin.site.register(OtherMedicalExpenses11, AdminOtherMedicalExpenses11)
admin.site.register(OtherMedicalExpenses10, AdminOtherMedicalExpenses10)
admin.site.register(OtherMedicalExpenses09, AdminOtherMedicalExpenses09)
admin.site.register(OtherMedicalExpenses08, AdminOtherMedicalExpenses08)
admin.site.register(OtherMedicalExpenses07, AdminOtherMedicalExpenses07)
admin.site.register(OtherMedicalExpenses06, AdminOtherMedicalExpenses06)
admin.site.register(OtherMedicalExpenses05, AdminOtherMedicalExpenses05)
admin.site.register(HospitalInpatientStays18, AdminHospitalInpatientStays18)
admin.site.register(HospitalInpatientStays17, AdminHospitalInpatientStays17)
admin.site.register(HospitalInpatientStays16, AdminHospitalInpatientStays16)
admin.site.register(HospitalInpatientStays15, AdminHospitalInpatientStays15)
admin.site.register(HospitalInpatientStays14, AdminHospitalInpatientStays14)
admin.site.register(HospitalInpatientStays13, AdminHospitalInpatientStays13)
admin.site.register(HospitalInpatientStays12, AdminHospitalInpatientStays12)
admin.site.register(HospitalInpatientStays11, AdminHospitalInpatientStays11)
admin.site.register(HospitalInpatientStays10, AdminHospitalInpatientStays10)
admin.site.register(HospitalInpatientStays09, AdminHospitalInpatientStays09)
admin.site.register(HospitalInpatientStays08, AdminHospitalInpatientStays08)
admin.site.register(HospitalInpatientStays07, AdminHospitalInpatientStays07)
admin.site.register(HospitalInpatientStays06, AdminHospitalInpatientStays06)
admin.site.register(HospitalInpatientStays05, AdminHospitalInpatientStays05)
admin.site.register(EmergencyRoomVisits18, AdminEmergencyRoomVisits18)
admin.site.register(EmergencyRoomVisits17, AdminEmergencyRoomVisits17)
admin.site.register(EmergencyRoomVisits16, AdminEmergencyRoomVisits16)
admin.site.register(EmergencyRoomVisits15, AdminEmergencyRoomVisits15)
admin.site.register(EmergencyRoomVisits14, AdminEmergencyRoomVisits14)
admin.site.register(EmergencyRoomVisits13, AdminEmergencyRoomVisits13)
admin.site.register(EmergencyRoomVisits12, AdminEmergencyRoomVisits12)
admin.site.register(EmergencyRoomVisits11, AdminEmergencyRoomVisits11)
admin.site.register(EmergencyRoomVisits10, AdminEmergencyRoomVisits10)
admin.site.register(EmergencyRoomVisits09, AdminEmergencyRoomVisits09)
admin.site.register(EmergencyRoomVisits08, AdminEmergencyRoomVisits08)
admin.site.register(EmergencyRoomVisits07, AdminEmergencyRoomVisits07)
admin.site.register(EmergencyRoomVisits06, AdminEmergencyRoomVisits06)
admin.site.register(EmergencyRoomVisits05, AdminEmergencyRoomVisits05)
admin.site.register(OutpatientVisits18, AdminOutpatientVisits18)
admin.site.register(OutpatientVisits17, AdminOutpatientVisits17)
admin.site.register(OutpatientVisits16, AdminOutpatientVisits16)
admin.site.register(OutpatientVisits15, AdminOutpatientVisits15)
admin.site.register(OutpatientVisits14, AdminOutpatientVisits14)
admin.site.register(OutpatientVisits13, AdminOutpatientVisits13)
admin.site.register(OutpatientVisits12, AdminOutpatientVisits12)
admin.site.register(OutpatientVisits11, AdminOutpatientVisits11)
admin.site.register(OutpatientVisits10, AdminOutpatientVisits10)
admin.site.register(OutpatientVisits09, AdminOutpatientVisits09)
admin.site.register(OutpatientVisits08, AdminOutpatientVisits08)
admin.site.register(OutpatientVisits07, AdminOutpatientVisits07)
admin.site.register(OutpatientVisits06, AdminOutpatientVisits06)
admin.site.register(OutpatientVisits05, AdminOutpatientVisits05)
admin.site.register(OfficeBasedVisits18, AdminOfficeBasedVisits18)
admin.site.register(OfficeBasedVisits17, AdminOfficeBasedVisits17)
admin.site.register(OfficeBasedVisits16, AdminOfficeBasedVisits16)
admin.site.register(OfficeBasedVisits15, AdminOfficeBasedVisits15)
admin.site.register(OfficeBasedVisits14, AdminOfficeBasedVisits14)
admin.site.register(OfficeBasedVisits13, AdminOfficeBasedVisits13)
admin.site.register(OfficeBasedVisits12, AdminOfficeBasedVisits12)
admin.site.register(OfficeBasedVisits11, AdminOfficeBasedVisits11)
admin.site.register(OfficeBasedVisits10, AdminOfficeBasedVisits10)
admin.site.register(OfficeBasedVisits09, AdminOfficeBasedVisits09)
admin.site.register(OfficeBasedVisits08, AdminOfficeBasedVisits08)
admin.site.register(OfficeBasedVisits07, AdminOfficeBasedVisits07)
admin.site.register(OfficeBasedVisits06, AdminOfficeBasedVisits06)
admin.site.register(OfficeBasedVisits05, AdminOfficeBasedVisits05)
admin.site.register(HomeHealth18, AdminHomeHealth18)
admin.site.register(HomeHealth17, AdminHomeHealth17)
admin.site.register(HomeHealth16, AdminHomeHealth16)
admin.site.register(HomeHealth15, AdminHomeHealth15)
admin.site.register(HomeHealth14, AdminHomeHealth14)
admin.site.register(HomeHealth13, AdminHomeHealth13)
admin.site.register(HomeHealth12, AdminHomeHealth12)
admin.site.register(HomeHealth11, AdminHomeHealth11)
admin.site.register(HomeHealth10, AdminHomeHealth10)
admin.site.register(HomeHealth09, AdminHomeHealth09)
admin.site.register(HomeHealth08, AdminHomeHealth08)
admin.site.register(HomeHealth07, AdminHomeHealth07)
admin.site.register(HomeHealth06, AdminHomeHealth06)
admin.site.register(HomeHealth05, AdminHomeHealth05)
