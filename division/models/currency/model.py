from common.fields import create_char_field
from common.mixinUid import UidMixin
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models

class Currency(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')

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

    abacus_id = models.IntegerField(blank=True, null=True, verbose_name='abacus id')

    def __str__(self):
        return self.description

