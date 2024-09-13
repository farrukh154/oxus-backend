from django.db import models
from django.utils.translation import gettext_lazy as _
from accounting.models.chart_account.model import ChartAccount  

class GeneralLedger(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name=_("Name")
    )
    account = models.ForeignKey( 
        ChartAccount, 
        on_delete=models.CASCADE, 
        related_name="general_ledgers", 
        verbose_name=_("Account"),
        default= 1
    )

    class Meta:
        verbose_name = _("general ledger")
        verbose_name_plural = _("General Ledgers")

    def __str__(self):
        return self.name
