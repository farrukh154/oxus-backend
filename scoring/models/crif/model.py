from django.db import models
from django.utils.translation import gettext_lazy as _
from common.fields import create_char_field
from common.models.AbstractBaseModel import AbstractBaseModel
from request_credit.models.r_credit.model import RequestCredit
from django.conf import settings

class CRIF(AbstractBaseModel):
    class Meta:
        verbose_name = _("CRIF")
        verbose_name_plural = _("CRIFs")

        permissions = (
            ('can-crif-get-information-abacus_crif', 'Custom: Can crif get information (abacus)'),
            ('can-crif-get-information-swift_crif', 'Custom: Can crif get information (swift)'),
            ('can-crif-generate-client-report_crif', 'Custom: Can crif generate client report'),
        )

    request_credit = models.ForeignKey(
        RequestCredit,
        on_delete=models.CASCADE,
        verbose_name="Swift id",
        null=True,
        blank=True,
    )
    abacus_customer_id = models.IntegerField(
        verbose_name='Абакус клиент Id',
        blank=True,
        null=True,
    )
    abacus_credit_id = models.IntegerField(
        verbose_name='Абакус кредит Id',
        blank=True,
        null=True,
    )
    abacus_account_number = create_char_field(
        max_length=255,
        verbose_name=_('Абакус контракт коде'),
        null=True,
        blank=True
    )
    data = models.JSONField(verbose_name=_('data'))
    has_not_history = models.BooleanField('has not history', default=False)
    crif_credit_id = create_char_field(
        max_length=255,
        verbose_name=_('код контракта в КИБТ'),
        null=True,
        blank=True
    )
    type = models.ForeignKey(
        to='scoring.ScoringType',
        on_delete=models.PROTECT,
        verbose_name="type",
    )
    parent = models.ForeignKey(
        to='scoring.CRIF',
        on_delete=models.PROTECT,
        verbose_name="parent",
        null=True,
        blank=True
    )
    generated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('generated by'),
        editable=False,
        null=True,
        on_delete=models.PROTECT,
    )


    def __str__(self):
        return f"{self.id}"