from django import template

register = template.Library()

data = {
  '01': { 'display_en': 'The entreprise', 'display_ru': 'Предприятие'},
  '02': { 'display_en': 'Building', 'display_ru': 'Здание'},
  '03': { 'display_en': 'Construсtions', 'display_ru': 'Постройка'},
  '04': { 'display_en': 'Apartment houses', 'display_ru': 'Жилые дома'},
  '05': { 'display_en': 'Apartments in apartment house', 'display_ru': 'Квартиры в жилом доме'},
  '06': { 'display_en': 'Part of apartment', 'display_ru': 'Часть квартиры'},
  '07': { 'display_en': 'Summer residence', 'display_ru': 'Летнее место жительства'},
  '08': { 'display_en': 'Incomplete building', 'display_ru': 'Недостроенное здание'},
  '09': { 'display_en': 'Land tenure rights', 'display_ru': 'Права землевладения'},
  '10': { 'display_en': 'Other real estate', 'display_ru': 'Другое недвижимое имущество'},
  '11': { 'display_en': 'Valuable papers', 'display_ru': 'Ценные бумаги'},
  '12': { 'display_en': 'Valuable papers - Bond', 'display_ru': 'Ценные бумаги - Облигация'},
  '13': { 'display_en': 'Valuable papers - Share', 'display_ru': 'Ценные бумаги - Акция'},
  '14': { 'display_en': 'Valuable papers - Bill', 'display_ru': 'Ценные бумаги - Вексель'},
  '15': { 'display_en': 'Valuable papers - Promissory note', 'display_ru': 'Ценные бумаги - Простой вексель'},
  '16': { 'display_en': 'Valuable papers - Deposit certificate', 'display_ru': 'Ценные бумаги - Депозитный сертификат'},
  '17': { 'display_en': 'Valuable papers - Commercial paper', 'display_ru': 'Ценные бумаги - Оборотные кредитно-денежные документы'},
  '18': { 'display_en': 'Valuable papers - Other paper valuated as money', 'display_ru': 'Ценные бумаги - Другая бумага, оцененная как деньги'},
  '19': { 'display_en': 'Metal, precious stone', 'display_ru': 'Металлы, драгоценные камни'},
  '20': { 'display_en': 'Machines, equipments, raw materials, goods', 'display_ru': 'Машины, оборудование, сырье, товары'},
  '21': { 'display_en': 'Machines, equipments, raw materials, goods - Machines, equipments', 'display_ru': 'Машины, оборудование, сырье, товары - Машины, оборудование'},
  '22': { 'display_en': 'Machines, equipments, raw materials, goods - Production line', 'display_ru': 'Машины, оборудование, сырье, товары - Поточная линия'},
  '23': { 'display_en': 'Machines, equipments, raw materials, goods - Raw materials', 'display_ru': 'Машины, оборудование, сырье, товары - Сырье'},
  '24': { 'display_en': 'Machines, equipments, raw materials, goods - Consumer product', 'display_ru': 'Машины, оборудование, сырье, товары - Потребительский товар'},
  '25': { 'display_en': 'Machines, equipments, raw materials, goods - Other goods', 'display_ru': 'Машины, оборудование, сырье, товары - Другие товары'},
  '26': { 'display_en': 'Other assets that have registered proprietary right and use right', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности'},
  '27': { 'display_en': 'Other assets that have registered proprietary right and use right - Asset right arising from copyright ', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Право актива как результат авторского права'},
  '28': { 'display_en': 'Other assets that have registered proprietary right and use right - Industrial proprietary right', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Индустриальное право собственности'},
  '29': { 'display_en': 'Other assets that have registered proprietary right and use right - Right of debt collection', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Право на взыскание долга'},
  '30': { 'display_en': 'Other assets that have registered proprietary right and use right - Right to be insured ', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Право на страхование'},
  '31': { 'display_en': 'Other assets that have registered proprietary right and use right - Right of capital contribution to enterprise', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Право на основной вклад в предприятие'},
  '32': { 'display_en': 'Other assets that have registered proprietary right and use right - Right of natural resource exploitation ', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Право на использование природных ресурсов'},
  '33': { 'display_en': 'Other assets that have registered proprietary right and use right - Income and rights arising from pledged asset', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Доход и права на заложенное имущество'},
  '34': { 'display_en': 'Other assets that have registered proprietary right and use right - Other right of assets', 'display_ru': 'Другие активы, которые регистрируют право использования и право собственности - Другое право на активы'},
  '35': { 'display_en': 'Other assets', 'display_ru': 'Другие активы'},
}

@register.filter
def crif_get_real_guarantees(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string