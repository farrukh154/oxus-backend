from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from division.models.region.model import Region

class Town(AbstractBaseModel):
    class Meta:
        verbose_name = _('town')
        verbose_name_plural = _('towns')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
        null=True,
        blank=True
    )

    abacus_id = models.BigIntegerField('abacus id', default=0)

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
    )

    active = models.BooleanField('active', default=True)

    def __str__(self):
        return self.name or 'town'
