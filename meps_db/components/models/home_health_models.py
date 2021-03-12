from django.db import models


class HomeHealth18(models.Model):
    """ Defines the HomeHealth Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    EVNTIDX = models.CharField("EVENT ID", max_length=16)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    DIETICN_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    IVTHP_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - IV OR INFUSION THERAPIST", max_length=2)
    MEDLDOC_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    OCCUPTHP_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - OCCUPATIONAL THERAP", max_length=2)
    PHYSLTHP_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - PHYSICAL THERAPY", max_length=2)
    RESPTHP_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW_M18 = models.CharField("TYPE OF PROF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP_M18 = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    HCarWrkrProfNone_M18 = models.CharField("NONE OF THE LISTED PROFESSIONAL HOME HEALTH PROVIDERS", max_length=2)
    COMPANN_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - COMPANION", max_length=2)
    HMEMAKER_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - HOMEMAKERHOUSE CLEANER", max_length=2)
    HHAIDE_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - HOME HEALTH  CARE AIDE", max_length=2)
    HOSPICE_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    NURAIDE_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    PERSONAL_M18 = models.CharField("TYPE OF NON PROF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    HCarWrkrNonProfNone_M18 = models.CharField(
        "NONE OF THE LISTED NON PROFESSIONAL HOME HEALTH PROVIDERS", max_length=2
    )
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    SAMESVCE_M18 = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2018", max_length=3)
    HHSF18X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR18X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD18X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV18X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA18X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR18X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=5)
    HHOF18X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    HHSL18X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC18X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR18X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU18X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT18X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP18X = models.CharField("SUM OF HHSF18X - HHOT18X (IMPUTED)", max_length=8)
    HHTC18X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth18 object"""
        return f"{self.DUPERSID}"


class HomeHealth17(models.Model):
    """ Defines the HomeHealth Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2017", max_length=2)
    HHSF17X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    HHMR17X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD17X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV17X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA17X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR17X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF17X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    HHSL17X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    HHWC17X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR17X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU17X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT17X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=6)
    HHXP17X = models.CharField("SUM OF HHSF17X - HHOT17X (IMPUTED)", max_length=8)
    HHTC17X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth17 object"""
        return f"{self.DUPERSID}"


class HomeHealth16(models.Model):
    """ Defines the HomeHealth Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=24)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2016", max_length=2)
    HHSF16X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    HHMR16X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD16X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV16X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA16X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR16X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=5)
    HHOF16X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    HHSL16X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC16X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR16X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU16X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT16X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP16X = models.CharField("SUM OF HHSF16X - HHOT16X (IMPUTED)", max_length=8)
    HHTC16X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth16 object"""
        return f"{self.DUPERSID}"


class HomeHealth15(models.Model):
    """ Defines the HomeHealth Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2015", max_length=2)
    HHSF15X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    HHMR15X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD15X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV15X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA15X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR15X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF15X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL15X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    HHWC15X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    HHOR15X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU15X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT15X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    HHXP15X = models.CharField("SUM OF HHSF15X - HHOT15X (IMPUTED)", max_length=8)
    HHTC15X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth15 object"""
        return f"{self.DUPERSID}"


class HomeHealth14(models.Model):
    """ Defines the HomeHealth Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2014", max_length=2)
    HHSF14X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR14X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD14X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV14X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA14X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR14X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=6)
    HHOF14X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    HHSL14X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC14X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    HHOR14X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU14X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=5)
    HHOT14X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    HHXP14X = models.CharField("SUM OF HHSF14X - HHOT14X (IMPUTED)", max_length=8)
    HHTC14X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth14 object"""
        return f"{self.DUPERSID}"


class HomeHealth13(models.Model):
    """ Defines the HomeHealth Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2013", max_length=2)
    HHSF13X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    HHMR13X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD13X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV13X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA13X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR13X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF13X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL13X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC13X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR13X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU13X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT13X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP13X = models.CharField("SUM OF HHSF13X - HHOT13X (IMPUTED)", max_length=8)
    HHTC13X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth13 object"""
        return f"{self.DUPERSID}"


class HomeHealth12(models.Model):
    """ Defines the HomeHealth Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=24)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2012", max_length=2)
    HHSF12X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR12X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD12X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV12X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA12X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR12X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=5)
    HHOF12X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL12X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC12X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR12X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU12X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    HHOT12X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=6)
    HHXP12X = models.CharField("SUM OF HHSF12X - HHOT12X (IMPUTED)", max_length=8)
    HHTC12X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth12 object"""
        return f"{self.DUPERSID}"


class HomeHealth11(models.Model):
    """ Defines the HomeHealth Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2011", max_length=2)
    HHSF11X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR11X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD11X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV11X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA11X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR11X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=5)
    HHOF11X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL11X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC11X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    HHOR11X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU11X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT11X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP11X = models.CharField("SUM OF HHSF11X - HHOT11X (IMPUTED)", max_length=8)
    HHTC11X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth11 object"""
        return f"{self.DUPERSID}"


class HomeHealth10(models.Model):
    """ Defines the HomeHealth Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2010", max_length=2)
    HHSF10X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR10X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD10X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV10X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA10X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=6)
    HHTR10X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF10X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL10X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC10X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    HHOR10X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU10X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT10X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP10X = models.CharField("SUM OF HHSF10X - HHOT10X (IMPUTED)", max_length=8)
    HHTC10X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth10 object"""
        return f"{self.DUPERSID}"


class HomeHealth09(models.Model):
    """ Defines the HomeHealth Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2009", max_length=2)
    HHSF09X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    HHMR09X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD09X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV09X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA09X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR09X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF09X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    HHSL09X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC09X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    HHOR09X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU09X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    HHOT09X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP09X = models.CharField("SUM OF HHSF09X - HHOT09X (IMPUTED)", max_length=8)
    HHTC09X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth09 object"""
        return f"{self.DUPERSID}"


class HomeHealth08(models.Model):
    """ Defines the HomeHealth Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2008", max_length=2)
    HHSF08X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR08X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD08X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    HHPV08X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA08X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    HHTR08X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    HHOF08X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    HHSL08X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC08X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    HHOR08X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU08X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT08X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP08X = models.CharField("SUM OF HHSF08X - HHOT08X (IMPUTED)", max_length=8)
    HHTC08X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth08 object"""
        return f"{self.DUPERSID}"


class HomeHealth07(models.Model):
    """ Defines the HomeHealth Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2007", max_length=2)
    HHSF07X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR07X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD07X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV07X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA07X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=7)
    HHTR07X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=7)
    HHOF07X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    HHSL07X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC07X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    HHOR07X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU07X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    HHOT07X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP07X = models.CharField("SUM OF HHSF07X - HHOT07X (IMPUTED)", max_length=8)
    HHTC07X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth07 object"""
        return f"{self.DUPERSID}"


class HomeHealth06(models.Model):
    """ Defines the HomeHealth Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=2)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2006", max_length=2)
    HHSF06X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR06X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    HHMD06X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV06X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    HHVA06X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=6)
    HHTR06X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=5)
    HHOF06X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    HHSL06X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    HHWC06X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=5)
    HHOR06X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU06X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    HHOT06X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=6)
    HHXP06X = models.CharField("SUM OF HHSF06X - HHOT06X (IMPUTED)", max_length=8)
    HHTC06X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth06 object"""
        return f"{self.DUPERSID}"


class HomeHealth05(models.Model):
    """ Defines the HomeHealth Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HomeHealth"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    HHDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    HHDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    MPCELIG = models.CharField("MPC ELIGIBILITY FLAG", max_length=1)
    SELFAGEN = models.CharField("DOES PROVIDER WORK FOR AGENCY OR SELF", max_length=2)
    HHTYPE = models.CharField("HOME HEALTH EVENT TYPE", max_length=1)
    CNA = models.CharField("TYPE OF HLTH CARE WRKR - CERT NURSE ASST", max_length=2)
    COMPANN = models.CharField("TYPE OF HLTH CARE WRKR - COMPANION", max_length=2)
    DIETICN = models.CharField("TYPE OF HLTH CARE WRKR - DIETITIANNUTRT", max_length=2)
    HHAIDE = models.CharField("TYPE OF HLTH CARE WRKR - HOME CARE AIDE", max_length=2)
    HOSPICE = models.CharField("TYPE OF HLTH CARE WRKR - HOSPICE WORKER", max_length=2)
    HMEMAKER = models.CharField("TYPE OF HLTH CARE WRKR - HOMEMAKER", max_length=2)
    IVTHP = models.CharField("TYPE OF HLTH CARE WRKR - IV THERAPIST", max_length=2)
    MEDLDOC = models.CharField("TYPE OF HLTH CARE WRKR - MEDICAL DOCTOR", max_length=2)
    NURPRACT = models.CharField("TYPE OF HLTH CARE WRKR - NURSEPRACTR", max_length=2)
    NURAIDE = models.CharField("TYPE OF HLTH CARE WRKR - NURSE S AIDE", max_length=2)
    OCCUPTHP = models.CharField("TYPE OF HLTH CARE WRKR - OCCUP THERAP", max_length=2)
    PERSONAL = models.CharField("TYPE OF HLTH CARE WRKR - PERS CARE ATTDT", max_length=2)
    PHYSLTHP = models.CharField("TYPE OF HLTH CARE WRKR - PHYSICL THERAPY", max_length=2)
    RESPTHP = models.CharField("TYPE OF HLTH CARE WRKR - RESPIRA THERAPY", max_length=2)
    SOCIALW = models.CharField("TYPE OF HLTH CARE WRKR - SOCIAL WORKER", max_length=2)
    SPEECTHP = models.CharField("TYPE OF HLTH CARE WRKR - SPEECH THERAPY", max_length=2)
    OTHRHCW = models.CharField("TYPE OF HLTH CARE WRKR - OTHER", max_length=2)
    NONSKILL = models.CharField("TYPE OF HLTH CARE WRKR - NON-SKILLED", max_length=2)
    SKILLED = models.CharField("TYPE OF HLTH CARE WRKR - SKILLED", max_length=2)
    SKILLWOS = models.CharField("SPECIFY TYPE OF SKILLED WORKER", max_length=25)
    OTHCW = models.CharField("TYPE OF HLTH CARE WRKR - SOME OTHER", max_length=2)
    OTHCWOS = models.CharField("SPECIFY OTHER TYPE HEALTH CARE WORKER", max_length=25)
    HOSPITAL = models.CharField("ANY HH CARE SVCE DUE TO HOSPITALIZATION", max_length=2)
    VSTRELCN = models.CharField("ANY HH CARE SVCE RELATED TO HLTH COND", max_length=2)
    TREATMT = models.CharField("PERSON RECEIVED MEDICAL TREATMENT", max_length=2)
    MEDEQUIP = models.CharField("PERSON WAS TAUGHT USE OF MED EQUIPMENT", max_length=2)
    DAILYACT = models.CharField("PERSON WAS HELPED WITH DAILY ACTIVITIES", max_length=2)
    COMPANY = models.CharField("PERSON RECEIVED COMPANIONSHIP SERVICES", max_length=2)
    OTHSVCE = models.CharField("PERSON RECEIVED OTH HOME CARE SERVICES", max_length=2)
    OTHSVCOS = models.CharField("SPECIFY OTHER HOME CARE SRVCE RECEIVED", max_length=25)
    FREQCY = models.CharField("PROVIDER HELPED EVERY WEEKSOME WEEKS", max_length=2)
    DAYSPWK = models.CharField("# DAYS  WEEK PROVIDER CAME", max_length=2)
    DAYSPMO = models.CharField("# DAYS  MONTH PROVIDER CAME", max_length=2)
    HOWOFTEN = models.CharField("PROV CAME ONCE PER DAYMORE THAN ONCE", max_length=2)
    TMSPDAY = models.CharField("TIMESDAY PROVIDER CAME TO HOME TO HELP", max_length=2)
    HRSLONG = models.CharField("HOURS EACH VISIT LASTED", max_length=2)
    MINLONG = models.CharField("MINUTES EACH VISIT LASTED", max_length=2)
    SAMESVCE = models.CharField("ANY OTH MONS PER RECEIVED SAME SERVICES", max_length=2)
    HHDAYS = models.CharField("DAYS PER MONTH IN HOME HEALTH, 2005", max_length=2)
    HHSF05X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    HHMR05X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    HHMD05X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    HHPV05X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    HHVA05X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=7)
    HHTR05X = models.CharField("HC-AMTPD, TRICARECHAMPVA (IMPUTED)", max_length=6)
    HHOF05X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=5)
    HHSL05X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    HHWC05X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    HHOR05X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    HHOU05X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    HHOT05X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    HHXP05X = models.CharField("SUM OF HHSF05X - HHOT05X (IMPUTED)", max_length=8)
    HHTC05X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HomeHealth05 object"""
        return f"{self.DUPERSID}"
