from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from reports.models.report import Report
from django.db import models
from django.conf import settings
class ReportHistory(AbstractBaseModel):
    class Meta:
        verbose_name = _('report history')
        verbose_name_plural = _('report histories')

        permissions = (
            ('can-view-all-generated-report_reporthistory', 'Can view all generated report by other user'),
        )

    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, blank=True, null=True
    )

    info = models.JSONField(
        verbose_name=_("info"),
        blank=True,
        null=True
    )

    duration = models.PositiveIntegerField(verbose_name=_("duration"), blank=True, null=True)

    xlsx_report = models.FileField(verbose_name=_("report"), blank=True, null=True)

    generated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('generated by'),
        editable=False,
        null=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.id}'
