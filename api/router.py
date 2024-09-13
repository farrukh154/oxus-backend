from dynamic_rest import routers
from terminals.models.terminal.viewset import TerminalViewSet
from helpdesk.models.helpdesk.viewset import HelpdeskViewSet
from helpdesk.models.helpdesk_priority.viewset import HelpdeskPriorityViewSet
from helpdesk.models.helpdesk_status.viewset import HelpdeskStatusViewSet
from terminals.models.terminal_vendor.viewset import TerminalVendorViewSet
from scoring.models.crif.viewset import CRIFViewSet
from common.utils import get_model_meta
from request_credit.models.r_credit.viewset import RequestCreditViewSet
from request_credit.models.r_status.viewset import RequestStatusViewSet
from division.models.branch.viewset import BranchViewSet
from division.models.region.viewset import RegionViewSet
from division.models.town.viewset import TownViewSet
from division.models.district.viewset import DistrictViewSet
from division.models.currency.viewset import CurrencyViewSet
from division.models.currency_exchange.viewset import CurrencyExchangeViewSet
from request_credit.models.rejection_reason.viewset import RejectionReasonViewSet
from request_credit.models.credit_purpose.viewset import CreditPurposeViewSet
from request_credit.models.economic_activity.viewset import EconomicActivityViewSet
from request_credit.models.economic_activity_type.viewset import EconomicActivityTypeViewSet
from credits.models.credit_product.viewset import CreditProductViewSet
from users.viewset import UserViewSet
from reports.models.report.viewset import ReportViewSet
from reports.models.report_history.viewset import ReportHistoryViewSet
from scan.models.customer_scan.viewset import CustomerScanViewSet
from scan.models.customer_scan_type.viewset import CustomerScanTypeViewSet
from scan.models.credit_scan.viewset import CreditScanViewSet
from scan.models.credit_scan_type.viewset import CreditScanTypeViewSet
from scoring.models.scoring_type.viewset import ScoringTypeViewSet
from customer.models.customer.viewset import CustomerViewSet
from request_credit.models.client_decision.viewset import ClientDecisionViewSet
from accounting.models.general_ledger.viewset import GeneralLedgerViewSet
from accounting.models.chart_account.viewset import ChartAccountViewSet
from accounting.models.account.viewset import AccountViewset
router = routers.DynamicRouter()


def register(*views):
    for view in views:

        class View(
            view,
        ):
            pass

        router.register(
            f"{get_model_meta(view).app_label}/{view.serializer_class.get_plural_name()}",
            View,
        )


register(
    UserViewSet,
    TerminalViewSet,
    HelpdeskViewSet,
    HelpdeskPriorityViewSet,
    HelpdeskStatusViewSet,
    TerminalVendorViewSet,
    RequestCreditViewSet,
    RequestStatusViewSet,
    BranchViewSet,
    RegionViewSet,
    TownViewSet,
    DistrictViewSet,
    CurrencyViewSet,
    CurrencyExchangeViewSet,
    RejectionReasonViewSet,
    CreditPurposeViewSet,
    EconomicActivityTypeViewSet,
    EconomicActivityViewSet,
    CRIFViewSet,
    CreditProductViewSet,
    ReportViewSet,
    ReportHistoryViewSet,
    CustomerScanViewSet,
    CustomerScanTypeViewSet,
    CreditScanViewSet,
    CreditScanTypeViewSet,
    ScoringTypeViewSet,
    CustomerViewSet,
    ClientDecisionViewSet,
    GeneralLedgerViewSet,
    ChartAccountViewSet,
    AccountViewset,
)
