from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel


class CreditPurpose(AbstractBaseModel):
    class Meta:
        verbose_name = _('Credit purpose')
        verbose_name_plural = _('Credit purposes')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )

    code = create_char_field(
        max_length=255,
        verbose_name=_('code'),
    )

    def __str__(self):
        return self.name
