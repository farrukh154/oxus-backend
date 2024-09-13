from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from common.fields import create_char_field
from division.models.currency.model import Currency


class CurrencyExchange(AbstractBaseModel):
    class Meta:
        verbose_name = _('currency Exchange')
        verbose_name_plural = _('currency exchanges')

    date = models.DateField()

    rate = models.DecimalField(
        _("rate"), max_digits=12, decimal_places=4,
    )
    
    currency_from = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='currency_from',
    )

    currency_to = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='currency_to',
    )
    class Meta:
        unique_together = ('date', 'currency_from', 'currency_to')

    def __str__(self):
        return self.currency_from.description
