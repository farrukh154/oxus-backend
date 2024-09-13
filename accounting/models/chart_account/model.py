from django.db import models
from django.utils.translation import gettext_lazy as _

class ChartAccount(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name=_("Name")
    )
    ru_name = models.CharField(
        max_length=100, 
        verbose_name=_("Ru name")
    )
    tj_name = models.CharField(
        max_length=100, 
        verbose_name=_("TJ name")
    )
    account_number = models.PositiveIntegerField(
        verbose_name=_("Account Number"),
        default=0
    )
  
    class Meta:
        verbose_name = _("chart account")
        verbose_name_plural = _("Chart Accounts")

    def __str__(self):
        return self.name
