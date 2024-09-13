import numpy_financial as npf
import json

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponse

class PaymentSchedule(object):
    month_number = 0
    payment_amount = 0  # месячный платёж
    loan_repayment = 0  # возврат займа
    interest_payment = 0  # выплата процентов
    outstanding_amount = 0  # непогашенная сумма
    round_level = 4

    def __init__(self, round_level=4):
        self.round_level = round_level
        self.month_number = 0
        self.payment_amount = 0
        self.loan_repayment = 0
        self.interest_payment = 0
        self.outstanding_amount = 0

    def get_month_number(self):
        return self.month_number

    def get_payment_amount(self):
        return round(abs(self.payment_amount), self.round_level)

    def get_loan_repayment(self):
        return round(abs(self.loan_repayment), self.round_level)

    def get_interest_payment(self):
        return round(self.interest_payment, self.round_level)

    def get_outstanding_amount(self):
        return round(self.outstanding_amount, self.round_level)

    def __str__(self) -> str:
        return f'Месяц №{self.get_month_number()}. Месячный платеж: {self.get_payment_amount()}. Возврат займа: {self.get_loan_repayment()}. Выплата процентов: {self.get_interest_payment()}. Непогашенная сумма: {self.get_outstanding_amount()}'


def percentage(amount, perc):
    return float(amount) * (float(perc) / 100)


class LoanPaymentSchedule:
    loan_amount = 0
    loan_term = 0
    loan_grace_period = 0
    loan_interest = 0
    schedules = []

    def calculate(self, loan_amount, loan_term, loan_grace_period, loan_interest):
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.loan_grace_period = loan_grace_period
        self.loan_interest = loan_interest
        self.schedules = []

        self.create_zero_month()

        for month_number in range(1, loan_term + 1):
            self.calculate_month(month_number)

        return self.schedules

    def create_zero_month(self):
        zero_month = PaymentSchedule()
        zero_month.outstanding_amount = self.loan_amount
        self.schedules.append(zero_month)

    def calculate_month(self, month_number):
        month_schedule = PaymentSchedule()
        month_schedule.month_number = month_number
        month_schedule.interest_payment = self.calculate_interest_payment(month_number)
        month_schedule.loan_repayment = self.calculate_loan_repayment(month_number)
        month_schedule.outstanding_amount = self.calculate_outstanding_amount(month_number,
                                                                              month_schedule.loan_repayment)
        month_schedule.payment_amount = self.calculate_payment_amount(month_number, month_schedule.interest_payment)

        self.schedules.append(month_schedule)

    def calculate_interest_payment(self, month_number):  # выплата процентов
        return percentage(self.schedules[month_number - 1].outstanding_amount, self.loan_interest)

    def calculate_loan_repayment(self, month_number):  # возврат займа
        if month_number <= self.loan_grace_period:
            return 0
        if month_number > self.loan_term:
            return 0
        return npf.ppmt(self.loan_interest / 100, month_number - self.loan_grace_period,
                        self.loan_term - self.loan_grace_period, self.loan_amount, when=0)

    def calculate_outstanding_amount(self, month_number, current_month_loan_repayment):  # непогашенная сумма
        return self.schedules[month_number - 1].outstanding_amount + current_month_loan_repayment

    def calculate_payment_amount(self, month_number, current_month_interest_payment):  # месячный платеж
        if month_number <= self.loan_grace_period:
            return -current_month_interest_payment
        else:
            return npf.pmt(self.loan_interest / 100, self.loan_term - self.loan_grace_period, self.loan_amount)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_monthly_credit_payment(request):
    json_data = json.loads(request.body)
    amount = int(json_data['amount'])
    term = int(json_data['term'])
    grace_period = int(json_data['grace_period'])
    interest = float(json_data['interest'])

    result = LoanPaymentSchedule().calculate(amount, term, grace_period, interest)
    payment_amount = result[grace_period + 1].get_payment_amount()
    return HttpResponse(
        status=HTTP_200_OK,
        content=json.dumps(
            {
                'result': payment_amount
            }
        ),
        content_type="application/json"
    )