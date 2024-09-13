from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models


class EconomicActivity(AbstractBaseModel):
    class Meta:
        verbose_name = _('Economic activity')
        verbose_name_plural = _('Economic activities')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )

    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name
