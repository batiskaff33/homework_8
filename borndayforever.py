from random import randrange
PUSHKIN = {
        'born_year': 1799,
        'born_month': 6,
        'born_day': 6
        }

wrong_answers = ['Капец! Ответ неверный!', 'Стыдуха! Каждый россиянин должен знать ДР Саши Пушкина!', 'Ужос! Идите в библиотеку...']
global_break_statement = False

while True:
  try:
    input_year = int(input('Введите ГОД рождения Саши Пушкина?: '))
  except ValueError:
    print('Используйте только целое число!')
    continue
  if input_year != PUSHKIN['born_year']:
    print(str(input_year)+'?', wrong_answers[randrange(2)])
  else:
    print('Молодец! Верно..')
    while True:
        try:
            input_month = int(input('А в каком месяце родился Саша Пушкин? Введите номер: '))
        except ValueError:
            print('Используйте только целое число!')
            continue
        if input_month != PUSHKIN['born_month']:
            print(str(input_month) + '?', wrong_answers[randrange(2)])
        else:
            print('Молодец! Верно..')
            while True:
                try:
                    input_day = int(input('Ну а какого числа родился Саша Пушкин? Введите номер: '))
                except ValueError:
                    print('Используйте только целое число!')
                    continue
                if input_day != PUSHKIN['born_day']:
                    print(str(input_day) + '?', wrong_answers[randrange(2)])
                else:
                    print('Молодец! Верно... Пока, пока!')
                    global_break_statement = True
                    break
        if global_break_statement:
            break
    if global_break_statement:
        break
