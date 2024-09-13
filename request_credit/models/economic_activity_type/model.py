from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from request_credit.models.economic_activity.model import EconomicActivity


class EconomicActivityType(AbstractBaseModel):
    class Meta:
        verbose_name = _('Economic activity type')
        verbose_name_plural = _('Economic activities types')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )

    active = models.BooleanField(
        default=True,
    )

    economic_activity = models.ForeignKey(
        EconomicActivity,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name = 'Economic_activity'
    )

    def __str__(self):
        return self.name
