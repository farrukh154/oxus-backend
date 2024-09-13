from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from division.models.branch import Branch
from helpdesk.models.helpdesk_priority.model import Helpdesk_Priority
from helpdesk.models.helpdesk_status.model import Helpdesk_Status
from common.mixins import WhoDidItMixin

from users.models import User

class Helpdesk(AbstractBaseModel,WhoDidItMixin):
    class Meta:

        permissions = [
            ('can-view-all_helpdesk', 'Can view all helpdesks'),
        ]
        verbose_name = _("helpdesk")
        verbose_name_plural = _("helpdesk")

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
    )

    status = models.ForeignKey(
        Helpdesk_Status, on_delete=models.CASCADE, blank=True, null=True
    )

    priority = models.ForeignKey(
        Helpdesk_Priority, on_delete=models.CASCADE, blank=True, null=True
    )

    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, blank=True, null=True
    )

    for_whom = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )

    description = models.TextField(null=True)


    def __str__(self):
        return self.name

