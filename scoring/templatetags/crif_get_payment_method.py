from django import template

register = template.Library()

data = {
  'CAD': { 'display_en': 'Current Account Debit', 'display_ru': 'Дебет текущего счета'},
  'BOE': { 'display_en': 'Promissory Note', 'display_ru': 'Простой вексель'},
  'BAR': { 'display_en': 'Bank draft; Automated bank draft', 'display_ru': 'Банковский счет, автоматический банковский счет'},
  'DIR': { 'display_en': 'Direct transfer; postal payment slip', 'display_ru': 'Прямая передача; почтовая квитанция об оплате'},
  'ADD': { 'display_en': 'Authorization to Direct Current Account Debit (Standing Instruction)', 'display_ru': 'Непосредственный доступ дебету счета (действующая инструкция)'},
  'SAC': { 'display_en': 'Saving Account (Standing Instruction)', 'display_ru': 'Сберегательный счет (действующая инструкция)'},
  'CCR': { 'display_en': 'Credit card payment', 'display_ru': 'Платеж по кредитной карте'},
  'CHQ': { 'display_en': 'Cheque', 'display_ru': 'Чек'},
  'CAS': { 'display_en': 'Cash', 'display_ru': 'Наличные'},
  'OTH': { 'display_en': 'Other', 'display_ru': 'Другое'},
}

@register.filter
def crif_get_payment_method(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string