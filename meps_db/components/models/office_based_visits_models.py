from django.db import models


class OfficeBasedVisits18(models.Model):
    """ Defines the OfficeBasedVisits Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    EVNTIDX = models.CharField("EVENT ID", max_length=16)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=14)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEEDOC_M18 = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    DRSPLTY_M18 = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE_M18 = models.CharField("TYPE OF MED PERSON P TALKED TO ON VISIT DT", max_length=3)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VISIT DT", max_length=3)
    VSTRELCN_M18 = models.CharField("THIS VISIT RELATED TO SPEC COND", max_length=2)
    LABTEST_M18 = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM_M18 = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS_M18 = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG_M18 = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI_M18 = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG_M18 = models.CharField("THIS VISIT DID P HAVE AN EKG, EEG OR ECG", max_length=2)
    RCVVAC_M18 = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF18 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2018", max_length=3)
    FFTOT19 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2018", max_length=3)
    OBSF18X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR18X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD18X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OBPV18X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=9)
    OBVA18X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR18X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=8)
    OBOF18X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=8)
    OBSL18X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC18X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR18X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU18X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT18X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP18X = models.CharField("SUM OF OBSF18X - OBOT18X (IMPUTED)", max_length=9)
    OBTC18X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits18 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits17(models.Model):
    """ Defines the OfficeBasedVisits Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG, EEG OR ECG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF17 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2017", max_length=2)
    FFTOT18 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2017", max_length=2)
    OBSF17X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR17X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD17X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV17X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA17X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR17X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF17X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL17X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OBWC17X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR17X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU17X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=8)
    OBOT17X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP17X = models.CharField("SUM OF OBSF17X - OBOT17X (IMPUTED)", max_length=8)
    OBTC17X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits17 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits16(models.Model):
    """ Defines the OfficeBasedVisits Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF16 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2016", max_length=2)
    FFTOT17 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2016", max_length=2)
    OBSF16X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR16X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD16X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV16X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA16X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OBTR16X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF16X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=8)
    OBSL16X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OBWC16X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR16X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU16X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=8)
    OBOT16X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP16X = models.CharField("SUM OF OBSF16X - OBOT16X (IMPUTED)", max_length=8)
    OBTC16X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits16 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits15(models.Model):
    """ Defines the OfficeBasedVisits Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF15 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2015", max_length=2)
    FFTOT16 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2015", max_length=2)
    OBSF15X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR15X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=9)
    OBMD15X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV15X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA15X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR15X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF15X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL15X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=9)
    OBWC15X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR15X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU15X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT15X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP15X = models.CharField("SUM OF OBSF15X - OBOT15X (IMPUTED)", max_length=9)
    OBTC15X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=10)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits15 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits14(models.Model):
    """ Defines the OfficeBasedVisits Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF14 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2014", max_length=2)
    FFTOT15 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2014", max_length=2)
    OBSF14X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR14X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD14X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OBPV14X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA14X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR14X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=8)
    OBOF14X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL14X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC14X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR14X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU14X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT14X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP14X = models.CharField("SUM OF OBSF14X - OBOT14X (IMPUTED)", max_length=8)
    OBTC14X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits14 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits13(models.Model):
    """ Defines the OfficeBasedVisits Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF13 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2013", max_length=2)
    FFTOT14 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2013", max_length=2)
    OBSF13X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR13X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD13X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV13X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA13X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR13X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF13X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL13X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC13X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR13X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU13X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT13X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP13X = models.CharField("SUM OF OBSF13X - OBOT13X (IMPUTED)", max_length=8)
    OBTC13X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits13 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits12(models.Model):
    """ Defines the OfficeBasedVisits Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF12 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2012", max_length=2)
    FFTOT13 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2012", max_length=2)
    OBSF12X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR12X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD12X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV12X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA12X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR12X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF12X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL12X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OBWC12X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR12X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OBOU12X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT12X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OBXP12X = models.CharField("SUM OF OBSF12X - OBOT12X (IMPUTED)", max_length=8)
    OBTC12X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits12 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits11(models.Model):
    """ Defines the OfficeBasedVisits Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF11 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2011", max_length=2)
    FFTOT12 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2011", max_length=2)
    OBSF11X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR11X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD11X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV11X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA11X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR11X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=8)
    OBOF11X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL11X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC11X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR11X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OBOU11X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=8)
    OBOT11X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OBXP11X = models.CharField("SUM OF OBSF11X - OBOT11X (IMPUTED)", max_length=8)
    OBTC11X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=13)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits11 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits10(models.Model):
    """ Defines the OfficeBasedVisits Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF10 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2010", max_length=2)
    FFTOT11 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2010", max_length=2)
    OBSF10X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR10X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD10X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV10X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA10X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR10X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF10X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL10X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC10X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR10X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU10X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT10X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP10X = models.CharField("SUM OF OBSF10X - OBOT10X (IMPUTED)", max_length=8)
    OBTC10X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits10 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits09(models.Model):
    """ Defines the OfficeBasedVisits Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF09 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2009", max_length=2)
    FFTOT10 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2009", max_length=2)
    OBSF09X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR09X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD09X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV09X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA09X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=8)
    OBTR09X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=8)
    OBOF09X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL09X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC09X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR09X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU09X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT09X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OBXP09X = models.CharField("SUM OF OBSF09X - OBOT09X (IMPUTED)", max_length=8)
    OBTC09X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits09 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits08(models.Model):
    """ Defines the OfficeBasedVisits Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF08 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2008", max_length=2)
    FFTOT09 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2008", max_length=2)
    OBSF08X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR08X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD08X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV08X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA08X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OBTR08X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OBOF08X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL08X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC08X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR08X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OBOU08X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT08X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OBXP08X = models.CharField("SUM OF OBSF08X - OBOT08X (IMPUTED)", max_length=8)
    OBTC08X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits08 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits07(models.Model):
    """ Defines the OfficeBasedVisits Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO3X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF07 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2007", max_length=2)
    FFTOT08 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2007", max_length=2)
    OBSF07X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR07X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD07X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV07X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA07X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=8)
    OBTR07X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=8)
    OBOF07X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL07X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OBWC07X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR07X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU07X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT07X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP07X = models.CharField("SUM OF OBSF07X - OBOT07X (IMPUTED)", max_length=8)
    OBTC07X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits07 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits06(models.Model):
    """ Defines the OfficeBasedVisits Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    OTHSHOT = models.CharField("THIS VISIT DID P HAVE OTHER SHOT", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO3X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF06 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2006", max_length=2)
    FFTOT07 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2006", max_length=2)
    OBSF06X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR06X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD06X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OBPV06X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA06X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=8)
    OBTR06X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=7)
    OBOF06X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL06X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC06X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OBOR06X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU06X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OBOT06X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OBXP06X = models.CharField("SUM OF OBSF06X - OBOT06X (IMPUTED)", max_length=8)
    OBTC06X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits06 object"""
        return f"{self.DUPERSID}"


class OfficeBasedVisits05(models.Model):
    """ Defines the OfficeBasedVisits Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OfficeBasedVisits"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    OBDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    OBDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    OBDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEETLKPV = models.CharField("DID P VISIT PROV IN PERSON OR TELEPHONE", max_length=2)
    MVPLACE = models.CharField("KIND OF PLACE PATIENT SAW MV PROVIDER", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISITPHONE CALL", max_length=2)
    DRSPLTY = models.CharField("MVIS DOCTOR S SPECIALTY", max_length=2)
    MEDPTYPE = models.CharField("TYPE OF MED PERSON P TALKED TO ON VST DT", max_length=2)
    DOCATLOC = models.CharField("ANY MD WORK AT LOCATION WHERE P SAW PROV", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VSTPHONE CALL RELATED TO SPEC COND", max_length=2)
    PHYSTH = models.CharField("THIS VISIT DID P HAVE PHYSICAL THERAPY", max_length=2)
    OCCUPTH = models.CharField("THIS VIS DID P HAVE OCCUPATIONAL THERAPY", max_length=2)
    SPEECHTH = models.CharField("THIS VISIT DID P HAVE SPEECH THERAPY", max_length=2)
    CHEMOTH = models.CharField("THIS VISIT DID P HAVE CHEMOTHERAPY", max_length=2)
    RADIATTH = models.CharField("THIS VISIT DID P HAVE RADIATION THERAPY", max_length=2)
    KIDNEYD = models.CharField("THIS VISIT DID P HAVE KIDNEY DIALYSIS", max_length=2)
    IVTHER = models.CharField("THIS VISIT DID P HAVE IV THERAPY", max_length=2)
    DRUGTRT = models.CharField("THIS VIS DID P HAVE TRT FOR DRUGALCOHOL", max_length=2)
    RCVSHOT = models.CharField("THIS VISIT DID P RECEIVE AN ALLERGY SHOT", max_length=2)
    PSYCHOTH = models.CharField("DID P HAVE PSYCHOTHERAPYCOUNSELING", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    OBICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    OBPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBPRO3X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    OBCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    OBCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFOBTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF05 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2005", max_length=2)
    FFTOT06 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2005", max_length=2)
    OBSF05X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OBMR05X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OBMD05X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=9)
    OBPV05X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OBVA05X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=8)
    OBTR05X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=7)
    OBOF05X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OBSL05X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OBWC05X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OBOR05X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OBOU05X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=8)
    OBOT05X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OBXP05X = models.CharField("SUM OF OBSF05X - OBOT05X (IMPUTED)", max_length=9)
    OBTC05X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OfficeBasedVisits05 object"""
        return f"{self.DUPERSID}"
