from django.db import models


class MedicalConditions18(models.Model):
    """ Defines the MedicalConditions Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions18"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=13)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=3)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=3)
    ICD10CDX = models.CharField("ICD-10-CM CODE FOR CONDITION - EDITED", max_length=3)
    CCSR1X = models.CharField("CLINICAL CLASSIFICATION REFINED CODE 1- EDITED", max_length=6)
    CCSR2X = models.CharField("CLINICAL CLASSIFICATION REFINED CODE 2- EDITED", max_length=6)
    CCSR3X = models.CharField("CLINICAL CLASSIFICATION REFINED CODE 3- EDITED", max_length=6)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions18 object"""
        return f"{self.DUPERSID}"


class MedicalConditions17(models.Model):
    """ Defines the MedicalConditions Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions17"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ICD10CDX = models.CharField("ICD-10-CM CODE FOR CONDITION - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions17 object"""
        return f"{self.DUPERSID}"


class MedicalConditions16(models.Model):
    """ Defines the MedicalConditions Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions16"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ICD10CDX = models.CharField("ICD-10-CM CODE FOR CONDITION - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions16 object"""
        return f"{self.DUPERSID}"


class MedicalConditions15(models.Model):
    """ Defines the MedicalConditions Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions15"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions15 object"""
        return f"{self.DUPERSID}"


class MedicalConditions14(models.Model):
    """ Defines the MedicalConditions Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions14"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions14 object"""
        return f"{self.DUPERSID}"


class MedicalConditions13(models.Model):
    """ Defines the MedicalConditions Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions13"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions13 object"""
        return f"{self.DUPERSID}"


class MedicalConditions12(models.Model):
    """ Defines the MedicalConditions Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions12"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=1)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=2)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=1)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions12 object"""
        return f"{self.DUPERSID}"


class MedicalConditions11(models.Model):
    """ Defines the MedicalConditions Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions11"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=1)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=1)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=13)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions11 object"""
        return f"{self.DUPERSID}"


class MedicalConditions10(models.Model):
    """ Defines the MedicalConditions Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions10"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=1)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=1)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=1)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions10 object"""
        return f"{self.DUPERSID}"


class MedicalConditions09(models.Model):
    """ Defines the MedicalConditions Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions09"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    PRIOLIST = models.CharField("IS CONDITION ON PRIORITY LIST", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND 1", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND 2", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND 3", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND 4", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND 5", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=1)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=1)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=1)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions09 object"""
        return f"{self.DUPERSID}"


class MedicalConditions08(models.Model):
    """ Defines the MedicalConditions Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions08"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    PRIOLIST = models.CharField("IS CONDITION ON PRIORITY LIST", max_length=1)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=1)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=2)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=1)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions08 object"""
        return f"{self.DUPERSID}"


class MedicalConditions07(models.Model):
    """ Defines the MedicalConditions Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions07"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    PRIOLIST = models.CharField("IS CONDITION ON PRIORITY LIST", max_length=1)
    CONDBEGD = models.CharField("DATE CONDITION STARTED -- DAY", max_length=2)
    CONDBEGM = models.CharField("DATE CONDITION STARTED -- MONTH", max_length=2)
    CONDBEGY = models.CharField("DATE CONDITION STARTED -- YEAR", max_length=4)
    SEEDREV3 = models.CharField("RD3: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV4 = models.CharField("RD4: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV5 = models.CharField("RD5: EVER SEEN DR FOR COND", max_length=2)
    STILTR3 = models.CharField("RD3: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR4 = models.CharField("RD4: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR5 = models.CharField("RD5: IS PERS STILL TREATED FOR COND", max_length=2)
    OVRALL3 = models.CharField("RD3: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL4 = models.CharField("RD4: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL5 = models.CharField("RD5: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    FURTCA3 = models.CharField("RD3: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA4 = models.CharField("RD4: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA5 = models.CharField("RD5: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FOLOCA3 = models.CharField("RD3: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA4 = models.CharField("RD4: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA5 = models.CharField("RD5: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    SEEDREF3 = models.CharField("RD3: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF4 = models.CharField("RD4: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF5 = models.CharField("RD5: SAW DR IN REFERENCE PERIOD", max_length=2)
    AGEDIAG = models.CharField("AGE WHEN DIAGNOSED", max_length=2)
    REMISSN = models.CharField("IS CANCER IN REMISSIONUNDER CONTROL", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    PRIORFLG = models.CharField("LOCATION OF RND SPECIFIC PRIORITY INFO", max_length=1)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=2)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNJAN = models.CharField("ACCIDENTINJURY OCCUR BEFOREAFTER JAN 1", max_length=2)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ACDNTLOC = models.CharField("WHERE DID ACCIDENT HAPPEN", max_length=2)
    INOUTHH = models.CharField("WAS ACCIDENT INSIDEOUTSIDE THE HOUSE", max_length=2)
    VEHICLE = models.CharField("WAS A MOTOR VEHICLE INVOLVED", max_length=2)
    WEAPON = models.CharField("WAS SOME OTHER WEAPON INVOLVED", max_length=2)
    POISON = models.CharField("WAS POISONPOISONOUS SUBSTANCE INVOLVED", max_length=2)
    FIREBURN = models.CharField("WAS FIREBURNING INVOLVED", max_length=2)
    DROWN = models.CharField("WAS DROWNINGNEAR-DROWNING INVOLVED", max_length=2)
    SPORTS = models.CharField("WAS IT A SPORTS INJURY", max_length=2)
    FALL = models.CharField("WAS IT A FALL", max_length=2)
    ACDNTOTH = models.CharField("WAS SOMETHING ELSE INVOLVED", max_length=2)
    RECOVER = models.CharField("FULLY RECOVERED FROM CONDITION", max_length=2)
    INJURFLG = models.CharField("LOCATION OF RND SPECIFIC INJURY INFO", max_length=1)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=2)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=2)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions07 object"""
        return f"{self.DUPERSID}"


class MedicalConditions06(models.Model):
    """ Defines the MedicalConditions Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions06"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    PRIOLIST = models.CharField("IS CONDITION ON PRIORITY LIST", max_length=1)
    CONDBEGD = models.CharField("DATE CONDITION STARTED -- DAY", max_length=2)
    CONDBEGM = models.CharField("DATE CONDITION STARTED -- MONTH", max_length=2)
    CONDBEGY = models.CharField("DATE CONDITION STARTED -- YEAR", max_length=4)
    SEEDREV1 = models.CharField("RD1: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV2 = models.CharField("RD2: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV3 = models.CharField("RD3: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV4 = models.CharField("RD4: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV5 = models.CharField("RD5: EVER SEEN DR FOR COND", max_length=2)
    LSTSAW1 = models.CharField("RD1: WHEN WAS LAST TIME DR WAS SEEN", max_length=2)
    STILTR1 = models.CharField("RD1: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR2 = models.CharField("RD2: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR3 = models.CharField("RD3: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR4 = models.CharField("RD4: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR5 = models.CharField("RD5: IS PERS STILL TREATED FOR COND", max_length=2)
    OVRALL1 = models.CharField("RD1: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL2 = models.CharField("RD2: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL3 = models.CharField("RD3: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL4 = models.CharField("RD4: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL5 = models.CharField("RD5: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    FURTCA1 = models.CharField("RD1: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA2 = models.CharField("RD2: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA3 = models.CharField("RD3: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA4 = models.CharField("RD4: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA5 = models.CharField("RD5: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FOLOCA1 = models.CharField("RD1: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA2 = models.CharField("RD2: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA3 = models.CharField("RD3: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA4 = models.CharField("RD4: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA5 = models.CharField("RD5: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    SEEDREF1 = models.CharField("RD1: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF2 = models.CharField("RD2: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF3 = models.CharField("RD3: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF4 = models.CharField("RD4: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF5 = models.CharField("RD5: SAW DR IN REFERENCE PERIOD", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    PRIORFLG = models.CharField("LOCATION OF RND SPECIFIC PRIORITY INFO", max_length=1)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=2)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ACDNTLOC = models.CharField("WHERE DID ACCIDENT HAPPEN", max_length=2)
    INOUTHH = models.CharField("WAS ACCIDENT INSIDEOUTSIDE THE HOUSE", max_length=2)
    VEHICLE = models.CharField("WAS A MOTOR VEHICLE INVOLVED", max_length=2)
    GUN = models.CharField("WAS A GUN INVOLVED", max_length=2)
    WEAPON = models.CharField("WAS SOME OTHER WEAPON INVOLVED", max_length=2)
    POISON = models.CharField("WAS POISONPOISONOUS SUBSTANCE INVOLVED", max_length=2)
    FIREBURN = models.CharField("WAS FIREBURNING INVOLVED", max_length=2)
    DROWN = models.CharField("WAS DROWNINGNEAR-DROWNING INVOLVED", max_length=2)
    SPORTS = models.CharField("WAS IT A SPORTS INJURY", max_length=2)
    FALL = models.CharField("WAS IT A FALL", max_length=2)
    ACDNTOTH = models.CharField("WAS SOMETHING ELSE INVOLVED", max_length=2)
    RECOVER = models.CharField("FULLY RECOVERED FROM CONDITION", max_length=2)
    INJURFLG = models.CharField("LOCATION OF RND SPECIFIC INJURY INFO", max_length=1)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=2)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=2)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=1)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=1)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions06 object"""
        return f"{self.DUPERSID}"


class MedicalConditions05(models.Model):
    """ Defines the MedicalConditions Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "MedicalConditions05"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    CONDN = models.CharField("CONDITION NUMBER", max_length=3)
    CONDIDX = models.CharField("CONDITION ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    CONDRN = models.CharField("CONDITION ROUND NUMBER", max_length=1)
    PRIOLIST = models.CharField("IS CONDITION ON PRIORITY LIST", max_length=1)
    CONDBEGD = models.CharField("DATE CONDITION STARTED -- DAY", max_length=2)
    CONDBEGM = models.CharField("DATE CONDITION STARTED -- MONTH", max_length=2)
    CONDBEGY = models.CharField("DATE CONDITION STARTED -- YEAR", max_length=4)
    SEEDREV1 = models.CharField("RD1: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV2 = models.CharField("RD2: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV3 = models.CharField("RD3: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV4 = models.CharField("RD4: EVER SEEN DR FOR COND", max_length=2)
    SEEDREV5 = models.CharField("RD5: EVER SEEN DR FOR COND", max_length=2)
    LSTSAW1 = models.CharField("RD1: WHEN WAS LAST TIME DR WAS SEEN", max_length=2)
    STILTR1 = models.CharField("RD1: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR2 = models.CharField("RD2: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR3 = models.CharField("RD3: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR4 = models.CharField("RD4: IS PERS STILL TREATED FOR COND", max_length=2)
    STILTR5 = models.CharField("RD5: IS PERS STILL TREATED FOR COND", max_length=2)
    OVRALL1 = models.CharField("RD1: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL2 = models.CharField("RD2: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL3 = models.CharField("RD3: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL4 = models.CharField("RD4: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    OVRALL5 = models.CharField("RD5: HOW COND AFFECT OVERALL HEALTH", max_length=2)
    FURTCA1 = models.CharField("RD1: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA2 = models.CharField("RD2: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA3 = models.CharField("RD3: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA4 = models.CharField("RD4: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FURTCA5 = models.CharField("RD5: FURTHER TREATMENT RECOMMENDED", max_length=2)
    FOLOCA1 = models.CharField("RD1: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA2 = models.CharField("RD2: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA3 = models.CharField("RD3: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA4 = models.CharField("RD4: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    FOLOCA5 = models.CharField("RD5: RCV FOLLOWUP CARE FOR CONDITION", max_length=2)
    SEEDREF1 = models.CharField("RD1: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF2 = models.CharField("RD2: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF3 = models.CharField("RD3: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF4 = models.CharField("RD4: SAW DR IN REFERENCE PERIOD", max_length=2)
    SEEDREF5 = models.CharField("RD5: SAW DR IN REFERENCE PERIOD", max_length=2)
    CRND1 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND2 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND3 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=1)
    CRND4 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    CRND5 = models.CharField("HAS CONDITION INFORMATION IN ROUND", max_length=2)
    PRIORFLG = models.CharField("LOCATION OF RND SPECIFIC PRIORITY INFO", max_length=1)
    INJURY = models.CharField("WAS CONDITION DUE TO ACCIDENTINJURY", max_length=2)
    ACCDENTD = models.CharField("DATE OF ACCIDENT -- DAY", max_length=2)
    ACCDENTM = models.CharField("DATE OF ACCIDENT -- MONTH", max_length=2)
    ACCDENTY = models.CharField("DATE OF ACCIDENT -- YEAR", max_length=4)
    ACCDNWRK = models.CharField("DID ACCIDENT OCCUR AT WORK", max_length=2)
    ACDNTLOC = models.CharField("WHERE DID ACCIDENT HAPPEN", max_length=2)
    INOUTHH = models.CharField("WAS ACCIDENT INSIDEOUTSIDE THE HOUSE", max_length=2)
    VEHICLE = models.CharField("WAS A MOTOR VEHICLE INVOLVED", max_length=2)
    GUN = models.CharField("WAS A GUN INVOLVED", max_length=2)
    WEAPON = models.CharField("WAS SOME OTHER WEAPON INVOLVED", max_length=2)
    POISON = models.CharField("WAS POISONPOISONOUS SUBSTANCE INVOLVED", max_length=2)
    FIREBURN = models.CharField("WAS FIREBURNING INVOLVED", max_length=2)
    DROWN = models.CharField("WAS DROWNINGNEAR-DROWNING INVOLVED", max_length=2)
    SPORTS = models.CharField("WAS IT A SPORTS INJURY", max_length=2)
    FALL = models.CharField("WAS IT A FALL", max_length=2)
    ACDNTOTH = models.CharField("WAS SOMETHING ELSE INVOLVED", max_length=2)
    RECOVER = models.CharField("FULLY RECOVERED FROM CONDITION", max_length=2)
    INJURFLG = models.CharField("LOCATION OF RND SPECIFIC INJURY INFO", max_length=1)
    MISSWORK = models.CharField("FLAG ASSOCIATED WITH MISSED WORK DAYS", max_length=2)
    MISSSCHL = models.CharField("FLAG ASSOCIATED WITH MISSED SCHOOL DAYS", max_length=1)
    INBEDFLG = models.CharField("FLAG ASSOCIATED WITH BED DAYS", max_length=2)
    ICD9CODX = models.CharField("ICD-9-CM CODE FOR CONDITION - EDITED", max_length=3)
    ICD9PROX = models.CharField("ICD-9-CM CODE FOR PROCEDURE - EDITED", max_length=2)
    CCCODEX = models.CharField("CLINICAL CLASSIFICATION CODE - EDITED", max_length=3)
    HHNUM = models.CharField("# HOME HEALTH EVENTS ASSOC. W CONDITION", max_length=2)
    IPNUM = models.CharField("# INPATIENT EVENTS ASSOC. W CONDITION", max_length=2)
    OPNUM = models.CharField("# OUTPATIENT EVENTS ASSOC. W CONDITION", max_length=3)
    OBNUM = models.CharField("# OFFICE-BASED EVENTS ASSOC W CONDITION", max_length=3)
    ERNUM = models.CharField("# ER EVENTS ASSOC. W CONDITION", max_length=2)
    RXNUM = models.CharField("# PRESCRIBED MEDICINES ASSOC. W COND.", max_length=2)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a MedicalConditions05 object"""
        return f"{self.DUPERSID}"
