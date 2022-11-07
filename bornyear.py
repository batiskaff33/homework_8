c_keys = ['corp_name', 'INN', 'total_purchases','locations', 'site', 'emails', 'IP','is_active', 'tags']
c_data = {
    'customer_1': [ 'ООО Рога и Копыта',
                 332711445,
                 123457863.00,
                 {
                     'address_1': {
                          'postal_code': '600015',
                          'city': 'Владимир',
                          'street': 'ул.Разина',
                          'building': '38',
                          'office': '303'
                          },
                      'address_2': {
                          'postal_code': '126001',
                          'city': 'Москва',
                          'street': 'ул.Никонорова',
                          'building': '77',
                          'office': '2'
                          }
                  },
                 'http://adwt.ru',
                 [ 'admin@adwt.ru', 'sale@adwt.ru' ],
                 '37.123.1.56',
                 True,
                 ('one small','two bigs', 'six middle')

                 ]
}

customers = {}

for k in c_data.keys():
  customers[k] = dict(zip(c_keys, c_data[k]))

print(customers, end='\n\n')

for c_k, c_v in customers.items():
  print(c_k+':',type(c_v))

  for p_k, p_v in c_v.items():
    print( ' '*2, p_k+',', type(p_v))