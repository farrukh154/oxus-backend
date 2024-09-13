from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class WhoDidItMixin(models.Model):
    class Meta:
        abstract = True

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
        editable=False,
        null=True,
        on_delete=models.PROTECT,
        related_name='+'
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('updated by'),
        editable=False,
        null=True,
        on_delete=models.PROTECT,
        related_name='+'
    )
