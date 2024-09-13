from django import template

register = template.Library()

data = {
  '201': { 'display_en': 'Payment guarantee ', 'display_ru': 'Платежная гарантия'},
  '202': { 'display_en': 'Guarantee ', 'display_ru': 'Гарантия'},
  '203': { 'display_en': 'Bill of exchange guarantee without guarantee of payment', 'display_ru': 'Гарантия векселя без гарантии оплаты'},
  '204': { 'display_en': 'Unlimited corporate liability', 'display_ru': 'Неограниченная корпоративная ответственность'},
  '205': { 'display_en': 'Specific corporate liability ', 'display_ru': 'Определенная корпоративная ответственность'},
  '206': { 'display_en': 'Pledge of trust ', 'display_ru': 'Залог доверия'},
}

@register.filter
def crif_get_personal_guarantees(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string