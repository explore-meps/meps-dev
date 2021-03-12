from django.db import models


class OtherMedicalExpenses18(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses18"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    EVNTIDX = models.CharField("EVENT ID", max_length=16)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPE_M18 = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=1)
    OMSF18X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    OMMR18X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD18X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV18X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA18X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR18X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=8)
    OMOF18X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=8)
    OMSL18X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OMWC18X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    OMOR18X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU18X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT18X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP18X = models.CharField("SUM OF OMSF18X-OMOT18X (IMPUTED)", max_length=8)
    OMTC18X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses18 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses17(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses17"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF17 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2017", max_length=2)
    OMSF17X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR17X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD17X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV17X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA17X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR17X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF17X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL17X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC17X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR17X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU17X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT17X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP17X = models.CharField("SUM OF OMSF17X-OMOT17X (IMPUTED)", max_length=8)
    OMTC17X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses17 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses16(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses16"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF16 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2016", max_length=2)
    OMSF16X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR16X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    OMMD16X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OMPV16X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA16X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR16X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF16X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OMSL16X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC16X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR16X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU16X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT16X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=8)
    OMXP16X = models.CharField("SUM OF OMSF16X-OMOT16X (IMPUTED)", max_length=8)
    OMTC16X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses16 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses15(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses15"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF15 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2015", max_length=2)
    OMSF15X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR15X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD15X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV15X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA15X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR15X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF15X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL15X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC15X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    OMOR15X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU15X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT15X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP15X = models.CharField("SUM OF OMSF15X-OMOT15X (IMPUTED)", max_length=8)
    OMTC15X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses15 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses14(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses14"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF14 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2014", max_length=2)
    FFTOT15 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2014", max_length=2)
    OMSF14X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR14X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD14X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV14X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA14X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR14X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF14X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OMSL14X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OMWC14X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    OMOR14X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU14X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT14X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP14X = models.CharField("SUM OF OMSF14X-OMOT14X (IMPUTED)", max_length=8)
    OMTC14X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses14 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses13(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses13"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF13 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2013", max_length=2)
    FFTOT14 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2013", max_length=2)
    OMSF13X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR13X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD13X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV13X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA13X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR13X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF13X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL13X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OMWC13X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR13X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=8)
    OMOU13X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT13X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP13X = models.CharField("SUM OF OMSF13X-OMOT13X (IMPUTED)", max_length=8)
    OMTC13X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses13 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses12(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses12"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFTOT13 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2012", max_length=2)
    OMSF12X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR12X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD12X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV12X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA12X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR12X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF12X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL12X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=8)
    OMWC12X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR12X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU12X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT12X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP12X = models.CharField("SUM OF OMSF12X-OMOT12X (IMPUTED)", max_length=8)
    OMTC12X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses12 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses11(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses11"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=24)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF11 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2011", max_length=2)
    OMSF11X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR11X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD11X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV11X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA11X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR11X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF11X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL11X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC11X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR11X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU11X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT11X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP11X = models.CharField("SUM OF OMSF11X-OMOT11X (IMPUTED)", max_length=8)
    OMTC11X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=13)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses11 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses10(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses10"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF10 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2010", max_length=2)
    OMSF10X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR10X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    OMMD10X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OMPV10X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    OMVA10X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR10X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF10X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OMSL10X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OMWC10X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    OMOR10X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU10X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT10X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=6)
    OMXP10X = models.CharField("SUM OF OMSF10X-OMOT10X (IMPUTED)", max_length=8)
    OMTC10X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses10 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses09(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses09"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF09 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2009", max_length=2)
    OMSF09X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR09X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD09X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV09X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA09X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR09X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=7)
    OMOF09X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL09X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OMWC09X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR09X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU09X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT09X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP09X = models.CharField("SUM OF OMSF09X-OMOT09X (IMPUTED)", max_length=8)
    OMTC09X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses09 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses08(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses08"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF08 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2008", max_length=2)
    OMSF08X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    OMMR08X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    OMMD08X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OMPV08X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA08X = models.CharField("AMOUNT PAID, VETERANSCHAMPVA(IMPUTED)", max_length=7)
    OMTR08X = models.CharField("AMOUNT PAID, TRICARE(IMPUTED)", max_length=6)
    OMOF08X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OMSL08X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC08X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR08X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU08X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT08X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=6)
    OMXP08X = models.CharField("SUM OF OMSF08X-OMOT08X (IMPUTED)", max_length=8)
    OMTC08X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses08 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses07(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses07"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF07 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2007", max_length=2)
    OMSF07X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR07X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    OMMD07X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV07X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA07X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=7)
    OMTR07X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=7)
    OMOF07X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL07X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=7)
    OMWC07X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR07X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=6)
    OMOU07X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=6)
    OMOT07X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP07X = models.CharField("SUM OF OMSF07X-OMOT07X (IMPUTED)", max_length=8)
    OMTC07X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses07 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses06(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses06"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF06 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2006", max_length=2)
    FFTOT07 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2006", max_length=2)
    OMSF06X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    OMMR06X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    OMMD06X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    OMPV06X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=7)
    OMVA06X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=7)
    OMTR06X = models.CharField("AMOUNT PAID, TRICARECHAMPVA (IMPUTED)", max_length=7)
    OMOF06X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=6)
    OMSL06X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC06X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    OMOR06X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU06X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT06X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP06X = models.CharField("SUM OF OMSF06X-OMOT06X (IMPUTED)", max_length=8)
    OMTC06X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses06 object"""
        return f"{self.DUPERSID}"


class OtherMedicalExpenses05(models.Model):
    """ Defines the OtherMedicalExpenses Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "OtherMedicalExpenses05"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    OMTYPEX = models.CharField("OTHER MEDICAL EXPENSE TYPE - EDITED", max_length=2)
    OMTYPE = models.CharField("OTHER MEDICAL EXPENSE TYPE", max_length=2)
    OMOTHOX = models.CharField("OMTYPE OTHER SPECIFY - EDITED", max_length=25)
    OMOTHOS = models.CharField("OMTYPE OTHER SPECIFY", max_length=25)
    FFOMTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF05 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2005", max_length=2)
    OMSF05X = models.CharField("AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    OMMR05X = models.CharField("AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    OMMD05X = models.CharField("AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    OMPV05X = models.CharField("AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)", max_length=8)
    OMVA05X = models.CharField("AMOUNT PAID, VETERANS (IMPUTED)", max_length=7)
    OMTR05X = models.CharField("HC-AMTPD, TRICARECHAMPVA (IMPUTED)", max_length=6)
    OMOF05X = models.CharField("AMOUNT PAID, OTHER FEDERAL (IMPUTED)", max_length=7)
    OMSL05X = models.CharField("AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)", max_length=6)
    OMWC05X = models.CharField("AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=6)
    OMOR05X = models.CharField("AMOUNT PAID, OTHER PRIVATE (IMPUTED)", max_length=7)
    OMOU05X = models.CharField("AMOUNT PAID, OTHER PUBLIC (IMPUTED)", max_length=7)
    OMOT05X = models.CharField("AMOUNT PAID, OTHER INSURANCE (IMPUTED)", max_length=7)
    OMXP05X = models.CharField("SUM OF OMSF05X-OMOT05X (IMPUTED)", max_length=8)
    OMTC05X = models.CharField("HHLD REPORTED TOTAL CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a OtherMedicalExpenses05 object"""
        return f"{self.DUPERSID}"
