from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models

class Branch(AbstractBaseModel):
    class Meta:
        verbose_name = _('branch')
        verbose_name_plural = _('branches')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )

    code = create_char_field(
        max_length=255,
        verbose_name=_('code'),
    )

    description = create_char_field(
        max_length=255,
        verbose_name=_('description'),
    )

    regional_branch = create_char_field(
        max_length=255,
        verbose_name=_('regional branch'),
    )

    active = models.BooleanField('active', default=True)

    abacus_id = models.BigIntegerField('abacus id', default=0)

    def __str__(self):
        return self.description
