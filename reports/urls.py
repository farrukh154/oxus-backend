from django.urls import path
from reports.report_generate.abacus_olb_per_loan import abacus_olb_per_loan
from reports.report_generate.abacus_llp_per_loan import abacus_llp_per_loan
from reports.report_generate.abacus_active_loan import abacus_active_loan
from reports.report_generate.abacus_disbursement import abacus_disbursement
from reports.report_generate.swift_loan import swift_loan
from reports.report_generate.swift_loan_break import swift_loan_break
from reports.report_generate.abacus_swift_loan import abacus_swift_loan
from reports.report_generate.swift_loan_client_decision import swift_loan_client_decision

urlpatterns = [
    path('report-abacus-olb-per-loan/', abacus_olb_per_loan, name='report_abacus_olb_per_loan'),
    path('report-abacus-llp-per-loan/', abacus_llp_per_loan, name='report_abacus_llp_per_loan'),
    path('report-abacus-active-loan/', abacus_active_loan, name='report_abacus_active_loan'),
    path('report-abacus-disbursement/', abacus_disbursement, name='report_abacus_disbursement'),
    path('report-swift-loan/', swift_loan, name='report_swift_loan'),
    path('report-swift-loan-break/', swift_loan_break, name='report_swift_loan_break'),
    path('report-abacus-swift-loan/', abacus_swift_loan, name='abacus_swift_loan'),
    path('report-swift-loan-client-decision/', swift_loan_client_decision, name='swift_loan_client_decision'),
]
