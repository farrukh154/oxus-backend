from django import template

register = template.Library()

data = {
  '10': {'display_en': 'Generic Consumer Loan', 'display_ru': 'Общий потребительский кредит'},
  '11': {'display_en': 'Generic Business Loan', 'display_ru': 'Общий бизнес кредит'},
  '12': {'display_en': 'Generic Small Business Loan', 'display_ru': 'Кредит для малого бизнеса'},
  '13': {'display_en': 'Vehicle Loan', 'display_ru': 'Ссуда транспортного средства'},
  '14': {'display_en': 'Retail Finance for Appliance Purchase', 'display_ru': 'Розничное финансирование для покупки аппарата'},
  '15': {'display_en': 'Mortgage', 'display_ru': 'Ипотека'},
  '16': {'display_en': 'Special Rate Mortgage', 'display_ru': 'Ипотека по специальной ставке'},
  '17': {'display_en': 'Home Renovation Loan', 'display_ru': 'Ссуда на реконструкцию дома'},
  '18': {'display_en': 'Home Equity Loan', 'display_ru': 'Кредит под залог имущества'},
  '19': {'display_en': 'Commercial Mortgage', 'display_ru': 'Коммерческая ипотека'},
  '20': {'display_en': 'Working Capital and Short Term Loan', 'display_ru': 'Оборотный капитал и краткосрочный кредит'},
  '21': {'display_en': 'Project and Long Term Financing', 'display_ru': 'Проектное и долговременное финансирование'},
  '22': {'display_en': 'Payday Loan', 'display_ru': 'Кредит под залог будущей зарплаты'},
  '23': {'display_en': 'Unsecured Loan', 'display_ru': 'Необеспеченный заем'},
  '24': {'display_en': 'Vehicle Leasing', 'display_ru': 'Аренда транспортного средства'},
  '25': {'display_en': 'Real Estate Leasing', 'display_ru': 'Аренда недвижимости'},
  '26': {'display_en': 'Equipment Leasing', 'display_ru': 'Аренда оборудования'},
  '27': {'display_en': 'Student Loans', 'display_ru': 'Образовательные кредиты'},
  '28': {'display_en': 'For Land Purchase', 'display_ru': 'Кредит на покупку земли'},
  '29': {'display_en': 'For Equipment Purchase', 'display_ru': 'Кредит на покупку оборудования'},
  '30': {'display_en': 'For Business Expansion', 'display_ru': 'Кредит на расширение бизнеса'},
  '31': {'display_en': 'For Fixed Asset Improvement', 'display_ru': 'Кредит на пополнение основного капитала'},
  '32': {'display_en': 'For Building Real Estate', 'display_ru': 'Кредит на строительство недвижимости'},
  '33': {'display_en': 'For Securities Purchase', 'display_ru': 'Кредит на покупку акций (например, маржинальное кредитование)'},
  '34': {'display_en': 'For Debt Consolidation', 'display_ru': 'Кредит на консолидацию задолженности'},
  '35': {'display_en': 'Payroll', 'display_ru': 'Платежная ведомость'},
  '36': {'display_en': 'For Insurance premium financing', 'display_ru': 'Кредит на финансирование страхового взноса'},
  '37': {'display_en': 'For Medical Care', 'display_ru': 'Кредит на медицинского обслуживания'},
  '38': {'display_en': 'Agricultural Loan', 'display_ru': 'Сельскохозяйственная ссуда'},
  '39': {'display_en': 'Education Loan', 'display_ru': 'Образовательный кредит'},
  '49': {'display_en': 'Other Instalment Credit Line', 'display_ru': 'Другая, погашаемая в рассрочку кредитная линия'},
  '50': {'display_en': 'Credit Card (Revolving)', 'display_ru': 'Кредитная карта (возобновляемая)'},
  '51': {'display_en': 'Charge Card (Payable in full each month)', 'display_ru': 'Платежная карточка (подлежащий полной оплате каждый месяц)'},
  '80': {'display_en': 'Overdraft', 'display_ru': 'Овердрафт'},
  '81': {'display_en': 'Receivables Financing', 'display_ru': 'Финансирование дебиторской задолженности'},
  '99': {'display_en': 'Other Not Instalment Credit Line', 'display_ru': 'Другая, непогашаемая в рассрочку кредитная линия'},
}

@register.filter
def crif_get_product(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string