from django import template

register = template.Library()

data = {
  '1': { 'display_en': 'Citizen Passport ', 'display_ru': 'Гражданский паспорт'},
  '2': { 'display_en': 'Citizen foreign Passport ', 'display_ru': 'Паспорт иностаранного гражаданина'},
  '3': { 'display_en': 'Foreign Passport', 'display_ru': 'Загран Паспорт'},
  '4': { 'display_en': 'Driving license', 'display_ru': 'Водительское удостоверение'},
  '5': { 'display_en': 'Old Citizen Passport', 'display_ru': 'Предыдущий гражданский паспорт'},
  '9': { 'display_en': 'Other', 'display_ru': 'Другое'},
}
@register.filter
def crif_get_doc_type(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string