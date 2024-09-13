from django import template

register = template.Library()

data = {
  '1': { 'display_en': 'Full Time', 'display_ru': 'Полный рабочий день'},
  '2': { 'display_en': 'Part Time', 'display_ru': 'Неполный рабочий день'},
  '3': { 'display_en': 'Self Employment', 'display_ru': 'Самостоятельная занятость'},
  '4': { 'display_en': 'Seasonal', 'display_ru': 'Периодическая занятость'},
  '5': { 'display_en': 'Not Employed', 'display_ru': 'Безработный'},
  '6': { 'display_en': 'Retired', 'display_ru': 'Уволен'},
  '7': { 'display_en': 'Student', 'display_ru': 'Студент'},
  '8': { 'display_en': 'Other', 'display_ru': 'Другое'},
}
@register.filter
def crif_get_employment_status(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string