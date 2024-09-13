from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel


class RejectionReason(AbstractBaseModel):
    class Meta:
        verbose_name = _('rejection reason')
        verbose_name_plural = _('rejection reasons')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )

    def __str__(self):
        return self.name
