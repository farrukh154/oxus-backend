from common.fields import create_char_field
from common.mixinUid import UidMixin
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from common.fields import create_char_field

REPORT_MODEL = 'report'
REPORT_ABACUS_OLB_PER_LOAN = 'abacus-olb-per-loan'
REPORT_ABACUS_ACTIVE_LOAN = 'abacus-active-loan'
REPORT_SWIFT_LOAN = 'swift-loan'
REPORT_SWIFT_LOAN_BREAK = 'swift-loan-break'
REPORT_ABACUS_SWIFT_LOAN = 'abacus-swift-loan'
REPORT_ABACUS_LLP_PER_LOAN = 'abacus-llp-per-loan'
REPORT_ABACUS_DISBURSEMENT = 'abacus-disbursement'
REPORT_SWIFT_LOAN_CLIENT_DECISION = 'swift-loan-client-decision'

class Report(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _('Reports')
        verbose_name_plural = _('Reports')

        permissions = (
            (f'{REPORT_MODEL}-{REPORT_ABACUS_OLB_PER_LOAN}_{REPORT_MODEL}', 'Report: Abacus OLB per loans'),
            (f'{REPORT_MODEL}-{REPORT_ABACUS_ACTIVE_LOAN}_{REPORT_MODEL}', 'Report: Abacus Active loans'),
            (f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN}_{REPORT_MODEL}', 'Report: Swift loans'),
            (f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_BREAK}_{REPORT_MODEL}', 'Report: Swift loans break down'),
            (f'{REPORT_MODEL}-{REPORT_ABACUS_SWIFT_LOAN}_{REPORT_MODEL}', 'Report: Abacus client list for Swift loan'),
            (f'{REPORT_MODEL}-{REPORT_ABACUS_LLP_PER_LOAN}_{REPORT_MODEL}', 'Report: Abacus OLB and LLP per loans'),
            (f'{REPORT_MODEL}-{REPORT_ABACUS_DISBURSEMENT}_{REPORT_MODEL}', 'Report: Abacus disbursement'),
            (f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_CLIENT_DECISION}_{REPORT_MODEL}', 'Report: Swift loans client decisions'),
        )


    report_name = create_char_field(
        max_length=255,
        verbose_name=_('report name'),
    )

    description = create_char_field(
        max_length = 255,
        verbose_name = "description",
        null=True,
        blank=True,
    )

    category = create_char_field(
        max_length = 255,
        verbose_name = "category"
    )

    def __str__(self):
        return self.report_name
