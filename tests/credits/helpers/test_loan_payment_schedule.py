import unittest

from credits.helpers.loan_payment_schedule import LoanPaymentSchedule


class TestLoanPaymentSchedule(unittest.TestCase):
    def test_calculate_full_example(self):
        loan_amount = 20_000
        loan_term = 48
        loan_grace_period = 3
        loan_interest = 3

        loan_payment_schedule = LoanPaymentSchedule()
        result = loan_payment_schedule.calculate(loan_amount, loan_term, loan_grace_period, loan_interest)
        for month_schedule in result:
            if month_schedule.get_month_number() == 0:
                self._test_values(month_schedule, 0, 0, 0, 20_000)
            if month_schedule.get_month_number() == 1:
                self._test_values(month_schedule, 600, 0, 600, 20_000)
            if month_schedule.get_month_number() == 4:
                self._test_values(month_schedule, 815.7035, 215.7035, 600.0, 19_784.2965)
            if month_schedule.get_month_number() == 18:
                self._test_values(month_schedule, 815.7035, 326.2709, 489.4326, 15_988.1489)
            if month_schedule.get_month_number() == 48:
                self._test_values(month_schedule, 815.7035, 791.9452, 23.7584, 0.0)

    def _test_values(self, month_schedule, payment_amount, loan_repayment, interest_payment, outstanding_amount):
        self.assertEqual(payment_amount, month_schedule.get_payment_amount())
        self.assertEqual(loan_repayment, month_schedule.get_loan_repayment())
        self.assertEqual(interest_payment, month_schedule.get_interest_payment())
        self.assertEqual(outstanding_amount, month_schedule.get_outstanding_amount())
