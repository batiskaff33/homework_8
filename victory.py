# -----------------------------------------------------------
# Программа ВИТОРИНА
# victory.py
#
# (C) 2022 Evgeny Davydov, Vladimir, Russia
# Released under GNU Public License (GPL)
# email dev@adwt.ru
# -----------------------------------------------------------

# Подключаем библиотеки
import random

# Инициируем переменные
WRONG_ANSWERS = [
    'Ответ неверный! Идите в библиотеку.',
    'Вы плохо учились в школе!',
    'Ответ нетипичен для русского гражданина.'
]

CELEBRITIES = {
    'Пушкин' : {
        'birthday': '06.06.1799',
        'full_name': 'А.С.Пушкин'
        },
    'Петр I' : {
        'birthday': '09.06.1672',
        'full_name': 'Пётр I Алексе́евич'
        },
    'Путин' : {
        'birthday': '07.10.1952',
        'full_name': 'Владимир Владимирович Путин'
        },
    'Толстой' : {
        'birthday': '09.09.1828',
        'full_name': 'Лев Николаевич Толстой'
        },
    'Суворов' : {
        'birthday': '24.11.1730',
        'full_name': 'Александр Васильевич Суворов'
        }
}

right_answers = 0;
errors = 0;

# Функции

# Тело программы

# Выбираем случайную знамениться
celebrities_keys = list(CELEBRITIES.keys())
rand_celebrity = random.choice(celebrities_keys)

# Цикл опроса по году рождения
while True:
  # rand_celebrity =  random.choice(celebrities_keys)
  try:
    input_celebrity_birthday_year = int(input('В каком году родился '
                                              + CELEBRITIES[rand_celebrity]['full_name'] + ': '))
  except ValueError:
    print('Используйте только целые числа!')
  if int(input_celebrity_birthday_year) != int(CELEBRITIES[rand_celebrity]['birthday'][-4:]):
    print('Хм...' + str(input_celebrity_birthday_year) + '?'
          + ' ', WRONG_ANSWERS[random.randrange(2)]
          + ' Попробуйте еще разок.')
    errors = errors + 1
    continue
  else:
    print('Молодец! Верно.', end='')
    right_answers = right_answers + 1

    # Допрос в цикле по дате рождения
    while True:
      try:
        input_celebrity_birthday_date = input('А знаете какого числа родился '
                                              + CELEBRITIES[rand_celebrity]['full_name']
                                              + '?' + ' Введите дату и месяц в формате dd.mm: ')
      except ValueError:
        print('Что-то не так с форматом ввода')
      if str(input_celebrity_birthday_date) != str(CELEBRITIES[rand_celebrity]['birthday'][:5]):
        print(str(input_celebrity_birthday_date) + '?' + WRONG_ANSWERS[random.randrange(2)])
        print('Попробуйте еще разок. ', end='')
        errors = errors + 1
      else:
        print('Молодец! Верно...')
        right_answers = right_answers + 1
        break

  breaking = input('Хотите закончить викторину  и узнать счет? да/нет: ')

  if breaking.lstrip().rstrip() == 'да':
    print('Результат викторины тут...')
    print(f'Правильных ответов: {right_answers} ({right_answers*100/(right_answers + errors)}%)')
    print(f'Ошибок: {errors} ({errors*100/(right_answers + errors)}%')
    break
  elif breaking.lstrip().rstrip() == 'нет':
    rand_celebrity = random.choice(celebrities_keys)