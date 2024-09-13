from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from division.models.town.model import Town

class District(AbstractBaseModel):
    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
        null=True,
        blank=True
    )

    abacus_id = models.BigIntegerField('abacus id', default=0)

    town = models.ForeignKey(
        Town,
        on_delete=models.CASCADE,
    )

    active = models.BooleanField('active', default=True)

    def __str__(self):
        return self.name or 'district'
