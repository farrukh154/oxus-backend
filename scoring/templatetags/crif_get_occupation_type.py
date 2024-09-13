from django import template

register = template.Library()

data = {
  '1': { 'display_en': 'Factory workers', 'display_ru': 'Рабочий на фабрике'},
  '2': { 'display_en': 'Skilled workers', 'display_ru': 'Квалифицированный рабочий'},
  '3': { 'display_en': 'Military – Private Soldier', 'display_ru': 'Вооруженные силы – рядовой'},
  '4': { 'display_en': 'Military – Officer', 'display_ru': 'Вооруженные силы – офицер'},
  '5': { 'display_en': 'University teacher', 'display_ru': 'Унивеситетский учитель'},
  '6': { 'display_en': 'Other teacher', 'display_ru': 'Другой учитель'},
  '7': { 'display_en': 'Professional', 'display_ru': 'Пофессионал'},
  '8': { 'display_en': 'Employee', 'display_ru': 'Сотрудник'},
  '9': { 'display_en': 'Manager/Executive', 'display_ru': 'Менеджер/Руководитель'},
  '10': { 'display_en': 'State/public sector employee', 'display_ru': 'Сотрудник государственного/общественного сектора'},
  '11': { 'display_en': 'Entrepreneur', 'display_ru': 'Предприниматель'},
}
@register.filter
def crif_get_occupation_type(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string