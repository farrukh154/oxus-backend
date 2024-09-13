from api.router import router
from django.urls import include
from django.urls import path
# from auth.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenObtainPairView
from api.me import MeView
from request_credit.utils.print_declaration import print_declaration
from request_credit.utils.print_protocol import print_protocol
from request_credit.utils.print_order import print_order
from request_credit.utils.print_request_credit import print_request_credit
from request_credit.utils.swift_search_client import swift_search_client
from request_credit.utils.swift_search_client_extra import swift_search_client_extra
from common.helpers.number_helper import number_to_words_tj_api
from credits.helpers.loan_payment_schedule import get_monthly_credit_payment
from users.views import change_password
from common.get_terminal_records import get_terminal_records
from common.terminal_payment_change_date import terminal_payment_change_date
from common.terminal_payment_change_contract import terminal_payment_change_contract
from common.abacus.search_abacus_client_id import search_abacus_client_id
from common.abacus.search_abacus_advanced import search_abacus_advanced
from common.crif.crif_abacus_check import crif_abacus_check
from common.crif.crif_swift_check import crif_swift_check
from common.crif.crif_generate_client_report import crif_generate_client_report
from division.utils.synchronize_nbt_currency import synchronize_nbt_currency
from common.helpers.file_upload import file_upload_endpoint

urlpatterns = [
    path('auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('print-declaration/<int:id>/', print_declaration, name='print_declaration'),
    path('print-request-credits/<int:id>/', print_request_credit, name='print_request_credit'),
    path('print-protocol/<int:id>/', print_protocol, name='print_protocol'),
    path('print-order/<int:id>/', print_order, name='print_order'),
    path('request_credit/search_client', swift_search_client, name='swift_search_client'),
    path('request_credit/search_client_extra', swift_search_client_extra, name='swift_search_client_extra'),
    path('get-number-in-string/<int:id>/', number_to_words_tj_api, name='number_to_words_tj_api'),
    path('get-monthly-credit-payment/', get_monthly_credit_payment, name='get_monthly_credit_payment'),
    path('get-terminal-records/', get_terminal_records, name='get_terminal_records'),
    path('terminal-payment-change-date/', terminal_payment_change_date, name='terminal_payment_change_date'),
    path('terminal-payment-change-contract/', terminal_payment_change_contract, name='terminal_payment_change_contract'),
    path('search-abacus-client-id/', search_abacus_client_id, name='search_abacus_client_id'),
    path('search-abacus-advances/', search_abacus_advanced, name='search_abacus_advanced'),
    path('crif-abacus-check/', crif_abacus_check, name='crif_abacus_check'),
    path('crif-swift-check/', crif_swift_check, name='crif_swift_check'),
    path('crif-generate-client-report/<int:id>/', crif_generate_client_report, name='crif_generate_client_report'),
    path('synchronize-nbt-currency/', synchronize_nbt_currency, name='synchronize_nbt_currency'),
    path('auth/me/', MeView.as_view()),
    path('black_list/', include('black_list.urls')),
    path('reports/', include('reports.urls')),
    path("", include(router.urls)),
    path('change-password/', change_password, name='change_password'),
    path('upload/', file_upload_endpoint),
]
