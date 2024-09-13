from django import template

register = template.Library()

data = {
  '10': { 'display_en': 'Agriculture', 'display_ru': 'Сельское хозяйство'},
  '11': { 'display_en': 'Agriculture-Growing ', 'display_ru': 'Сельское хозяйство-Растениеводство'},
  '12': { 'display_en': 'Agriculture-Growing-cotton growing', 'display_ru': 'Сельское хозяйство-Растениеводство-Хлопководство'},
  '13': { 'display_en': 'Agriculture-Growing-crops', 'display_ru': 'Сельское хозяйство-Растениеводство-Зерноводство'},
  '14': { 'display_en': 'Agriculture-Growing-gardening', 'display_ru': 'Сельское хозяйство-Растениеводство-Садовоство'},
  '15': { 'display_en': 'Agriculture-Growing-viticulture', 'display_ru': 'Сельское хозяйство-Растениеводство-Виноградарство'},
  '16': { 'display_en': 'Agriculture-Growing-potato growing', 'display_ru': 'Сельское хозяйство-Растениеводство-Картофелеводство'},
  '17': { 'display_en': 'Agriculture-Growing-other segment of growing', 'display_ru': 'Сельское хозяйство-Растениеводство-Прочие подотрасли растениеводства'},
  '18': { 'display_en': 'Agriculture-animal husbandry', 'display_ru': 'Сельское хозяйство-Животноводство'},
  '19': { 'display_en': 'Agriculture-animal husbandry-cattle', 'display_ru': 'Сельское хозяйство-Животноводство-Крупный рогатый скот'},
  '20': { 'display_en': 'Agriculture-animal husbandry-small cattle; sheep and goats', 'display_ru': 'Сельское хозяйство-Животноводство-Мелкий рогатый скот'},
  '21': { 'display_en': 'Agriculture-animal husbandry-horse breeding', 'display_ru': 'Сельское хозяйство-Животноводство-Коневодство'},
  '22': { 'display_en': 'Agriculture-animal husbandry-other segment of animal husbandry', 'display_ru': 'Сельское хозяйство-Животноводство-Прочие подотрасли животноводства'},
  '23': { 'display_en': 'Agriculture-poultry keeping', 'display_ru': 'Сельское хозяйство-Птицеводство'},
  '24': { 'display_en': 'Agriculture-Other', 'display_ru': 'Сельское хозяйство-Прочие'},
  '25': { 'display_en': 'Agriculture-Other-bee keeping', 'display_ru': 'Сельское хозяйство-Прочие-Пчеловодство'},
  '26': { 'display_en': 'Agriculture-Other-fish breeding', 'display_ru': 'Сельское хозяйство-Прочие-Рыбоводство'},
  '27': { 'display_en': 'Agriculture-Other-Procurement of agricultural products', 'display_ru': 'Сельское хозяйство-Прочие-Заготовки сельско-хозяйственной продукции'},
  '28': { 'display_en': 'Agriculture-Other-Purchasing mineral fertilizers, fuels and lubricants, replacement component for agriculture needs', 'display_ru': 'Сельское хозяйство-Прочие-Приобретение минеральных удобрений, ГСМ, запасных частей и другого для нужд  сельского хозяйства'},
  '29': { 'display_en': 'Agriculture-Other-Buying and selling agriculture production (apart from cotton)', 'display_ru': 'Сельское хозяйство-Прочие-Купля-продажа сельскохозяйтвенной продукции (кроме хлопка)'},
  '30': { 'display_en': 'Agriculture-Other-Buying and selling cotton', 'display_ru': 'Сельское хозяйство-Прочие-Купля-продажа хлопка'},
  '31': { 'display_en': 'Agriculture-Other-Other', 'display_ru': 'Сельское хозяйство-Прочие-Прочие'},
  '32': { 'display_en': 'Manufacturing', 'display_ru': 'Промышленность'},
  '33': { 'display_en': 'Manufacturing-Light industry', 'display_ru': 'Промышленность-Легкая промышленность'},
  '34': { 'display_en': 'Manufacturing-Light industry-food', 'display_ru': 'Промышленность-Легкая промышленность-пищевая'},
  '35': { 'display_en': 'Manufacturing-Light industry-textiles', 'display_ru': 'Промышленность-Легкая промышленность-текстильная'},
  '36': { 'display_en': 'Manufacturing-Light industry-sewing', 'display_ru': 'Промышленность-Легкая промышленность-швейная'},
  '37': { 'display_en': 'Manufacturing-Light industry-footwear', 'display_ru': 'Промышленность-Легкая промышленность-обувная'},
  '38': { 'display_en': 'Manufacturing-Light industry-furniture', 'display_ru': 'Промышленность-Легкая промышленность-производство мебели'},
  '39': { 'display_en': 'Manufacturing-Heavy industry', 'display_ru': 'Промышленность-Тяжёлая промышленность'},
  '40': { 'display_en': 'Manufacturing-Heavy industry-Mining industry', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность'},
  '41': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-gas', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-газ'},
  '42': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-petroleum, oil ', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-нефть'},
  '43': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-coal ', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-уголь'},
  '44': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-precious metal', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-драгоценные металлы'},
  '45': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-other', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-прочие'},
  '46': { 'display_en': 'Manufacturing-Heavy industry-Mining industry-electricity (generation)', 'display_ru': 'Промышленность-Тяжёлая промышленность-Добывающая промышленность-Электроэнергия (производство)'},
  '47': { 'display_en': 'Manufacturing-Heavy industry-Other segment heavy industry', 'display_ru': 'Промышленность-Тяжёлая промышленность-Прочие отрасли тяжелой промышленности'},
  '48': { 'display_en': 'Manufacturing-Purchasing energy resource', 'display_ru': 'Промышленность-Приобретение энергоносителей '},
  '49': { 'display_en': 'Manufacturing-Purchasing energy resource-fuels and lubricants', 'display_ru': 'Промышленность-Приобретение энергоносителей -ГСМ'},
  '50': { 'display_en': 'Manufacturing-Purchasing energy resource-electricity', 'display_ru': 'Промышленность-Приобретение энергоносителей -Электроэнергия'},
  '51': { 'display_en': 'Manufacturing-Purchasing energy resource-Coal', 'display_ru': 'Промышленность-Приобретение энергоносителей -Уголь'},
  '52': { 'display_en': 'Manufacturing-Purchasing energy resource-Gas', 'display_ru': 'Промышленность-Приобретение энергоносителей -Газ'},
  '53': { 'display_en': 'Manufacturing-Purchasing energy resource-Other', 'display_ru': 'Промышленность-Приобретение энергоносителей -Прочие '},
  '54': { 'display_en': 'Manufacturing-Buying and selling energy resources', 'display_ru': 'Промышленность-Купля-продажа энергоносителей '},
  '55': { 'display_en': 'Manufacturing-Buying and selling energy resources-fuels and lubricants', 'display_ru': 'Промышленность-Купля-продажа энергоносителей -ГСМ'},
  '56': { 'display_en': 'Manufacturing-Buying and selling energy resources-electricity', 'display_ru': 'Промышленность-Купля-продажа энергоносителей -Электроэнергия'},
  '57': { 'display_en': 'Manufacturing-Buying and selling energy resources-Coal', 'display_ru': 'Промышленность-Купля-продажа энергоносителей -Уголь'},
  '58': { 'display_en': 'Manufacturing-Buying and selling energy resources-Gas', 'display_ru': 'Промышленность-Купля-продажа энергоносителей -Газ'},
  '59': { 'display_en': 'Manufacturing-Buying and selling energy resources-Other', 'display_ru': 'Промышленность-Купля-продажа энергоносителей -Прочие '},
  '60': { 'display_en': 'Manufacturing-Buying and selling manufacturing production (apart from energy resources) within Tajikistan', 'display_ru': 'Промышленность-Купля-продажа промышленной продукции (кроме энергоносителей) внутри Республики '},
  '61': { 'display_en': 'Construction', 'display_ru': 'Строительство'},
  '62': { 'display_en': 'Construction-Manufacturing', 'display_ru': 'Строительство-Производственное'},
  '63': { 'display_en': 'Construction-Nonmanufacturing', 'display_ru': 'Строительство-Непроизводственное'},
  '64': { 'display_en': 'Construction-housing construction', 'display_ru': 'Строительство-Жилищное'},
  '65': { 'display_en': 'Construction-Buying and selling construction materials', 'display_ru': 'Строительство-Купля-продажа строительных материалов'},
  '66': { 'display_en': 'Construction-Other', 'display_ru': 'Строительство-Проие'},
  '67': { 'display_en': 'Transport', 'display_ru': 'Транспорт'},
  '68': { 'display_en': 'Transport-Air transport', 'display_ru': 'Транспорт-Авиационный '},
  '69': { 'display_en': 'Transport-Transport via railways', 'display_ru': 'Транспорт-Железнодорожный'},
  '70': { 'display_en': 'Transport-Land transport', 'display_ru': 'Транспорт-Автомобильный'},
  '71': { 'display_en': 'Transport-trade transport', 'display_ru': 'Транспорт-Торговля транспортными средствами'},
  '72': { 'display_en': 'Transport-Other', 'display_ru': 'Транспорт-Прочие'},
  '73': { 'display_en': 'Public catering', 'display_ru': 'Общественное питание'},
  '74': { 'display_en': 'Service', 'display_ru': 'Услуги'},
  '75': { 'display_en': 'Service-Consumer services and housing municipal economy', 'display_ru': 'Услуги-Бытовые и ЖКХ'},
  '76': { 'display_en': 'Service-Hotels', 'display_ru': 'Услуги-Гостиничные'},
  '77': { 'display_en': 'Service-Scientific-education', 'display_ru': 'Услуги-Научно-образовательные'},
  '78': { 'display_en': 'Service-Medical', 'display_ru': 'Услуги-Медицинские'},
  '79': { 'display_en': 'Service-Travel', 'display_ru': 'Услуги-Туристические'},
  '80': { 'display_en': 'Service-Transport', 'display_ru': 'Услуги-Транспортные '},
  '81': { 'display_en': 'Service-Communication', 'display_ru': 'Услуги-Связи'},
  '82': { 'display_en': 'Service-Other', 'display_ru': 'Услуги-Прочие'},
  '83': { 'display_en': 'External trade', 'display_ru': 'Внешняя торговля'},
  '84': { 'display_en': 'External trade-Export', 'display_ru': 'Внешняя торговля-Экспорт'},
  '85': { 'display_en': 'External trade-Export-cotton', 'display_ru': 'Внешняя торговля-Экспорт-хлопка'},
  '86': { 'display_en': 'External trade-Export-Other agroculture production (apart from cotton)', 'display_ru': 'Внешняя торговля-Экспорт-прочей сельскохозяйственной продукции (кроме хлопка)'},
  '87': { 'display_en': 'External trade-Export-aluminium', 'display_ru': 'Внешняя торговля-Экспорт-аллюминия'},
  '88': { 'display_en': 'External trade-Export-electricity', 'display_ru': 'Внешняя торговля-Экспорт-электроэнергии'},
  '89': { 'display_en': 'External trade-Export-other export goods', 'display_ru': 'Внешняя торговля-Экспорт-прочих экспортируемых товаров'},
  '90': { 'display_en': 'External trade-Import', 'display_ru': 'Внешняя торговля-Импорт'},
  '91': { 'display_en': 'External trade-Import-petrochemical product ', 'display_ru': 'Внешняя торговля-Импорт-нефтепродуктов'},
  '92': { 'display_en': 'External trade-Import-natural gas', 'display_ru': 'Внешняя торговля-Импорт-природного газа'},
  '93': { 'display_en': 'External trade-Import-domestic gas', 'display_ru': 'Внешняя торговля-Импорт-сжиженного газа'},
  '94': { 'display_en': 'External trade-Import-electricity', 'display_ru': 'Внешняя торговля-Импорт-электроэнергии'},
  '95': { 'display_en': 'External trade-Import-wheat', 'display_ru': 'Внешняя торговля-Импорт-пшеницы'},
  '96': { 'display_en': 'External trade-Import-sorrow', 'display_ru': 'Внешняя торговля-Импорт-муки'},
  '97': { 'display_en': 'External trade-Import-other foodstuffs', 'display_ru': 'Внешняя торговля-Импорт-прочих продуктов питания'},
  '98': { 'display_en': 'External trade-Import-construction / building materials', 'display_ru': 'Внешняя торговля-Импорт-стройматериалов'},
  '99': { 'display_en': 'External trade-Import-medicine', 'display_ru': 'Внешняя торговля-Импорт-медикаментов'},
  '100': { 'display_en': 'External trade-Import-transport', 'display_ru': 'Внешняя торговля-Импорт-транспортных средств'},
  '101': { 'display_en': 'External trade-Import-equipment', 'display_ru': 'Внешняя торговля-Импорт-оборудования'},
  '102': { 'display_en': 'External trade-Import-mineral fertilizers', 'display_ru': 'Внешняя торговля-Импорт-минеральных удобрений'},
  '103': { 'display_en': 'External trade-Import-other import goods', 'display_ru': 'Внешняя торговля-Импорт-прочих импортируемых товаров'},
  '104': { 'display_en': 'Financial intermediation', 'display_ru': 'Финансовое посредничество'},
  '105': { 'display_en': 'Consumption', 'display_ru': 'Потребление'},
  '106': { 'display_en': 'Consumption-Purchase consumer goods', 'display_ru': 'Потребление-Приобретение потребительских товаров'},
  '107': { 'display_en': 'Consumption-Mortgage', 'display_ru': 'Потребление-Ипотека (приобретение жилья)'},
  '108': { 'display_en': 'Consumption-Labour migration', 'display_ru': 'Потребление-Трудовая миграция'},
  '109': { 'display_en': 'Consumption-Car lending', 'display_ru': 'Потребление-Автокредитование'},
  '110': { 'display_en': 'Consumption-Other segments', 'display_ru': 'Потребление-Прочие отрасли'},
  '111': { 'display_en': 'Other industries', 'display_ru': 'Прочие отрасли'},
}

@register.filter
def crif_get_debt_reason(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string