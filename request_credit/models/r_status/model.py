from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from common.mixinUid import UidMixin

CREATED_UID = 'CREATED'
TO_UNDERWRITER_UID = 'TO-UNDERWRITER'
APPROVED_UID = 'APPROVED'
DENIED_UID = 'DENIED'
POSTPONED_UID = 'POSTPONED'
DISBURSED_UID = 'DISBURSED'
CLIENT_REFUSED_UID = 'CLIENT-REFUSED'
CLIENT_UNAVAILABLE_UID = 'CLIENT-UNAVAILABLE'

class RequestStatus(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _("request status")
        verbose_name_plural = _("request statuses")

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
    )

    def __str__(self):
        return self.name
