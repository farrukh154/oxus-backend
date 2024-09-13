from django import template

register = template.Library()

data = {
  '0': { 'display_en': 'Credit is not re-organized', 'display_ru': 'Кредит не реорганизован'},
  '1': { 'display_en': 'Credit is re-organized by simply updating the old contract', 'display_ru': 'Кредит реорганизован простым обновлением старого контракт'},
  '2': { 'display_en': 'Credit is re-organized by closing the old contract and creating a new one, while keeping a reference link between the two ', 'display_ru': 'Кредит реорганизован путем закрытия старого контракта и создания нового, учитывая связь между двумя последними'},
}

@register.filter
def crif_get_flg_reorg(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string