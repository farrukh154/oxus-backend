from common.fields import create_char_field
from common.mixinUid import UidMixin
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
class Helpdesk_Priority(AbstractBaseModel,UidMixin):
    class Meta:
        verbose_name = _('helpdesk priority')
        verbose_name_plural = _('helpdesk priorities')

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
    )


    def __str__(self):
        return self.name
