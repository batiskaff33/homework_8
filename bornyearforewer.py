from random import randrange
right_pushkin_birthday = 1799
wrong_answers = ['Капец! Ответ неверный!', 'Стыдуха! Каждый россиянин должен знать ДР Саши Пушкина!', 'Ужос! Идите в библиотеку...']
while True:
  try:
    input_pushkin_birthday = int(input('Введите год рождения Саши Пушкина?: '))
  except ValueError:
    print('Используйте только целое число!')
    continue
  if input_pushkin_birthday != right_pushkin_birthday:
    print(str(input_pushkin_birthday)+'?', wrong_answers[randrange(2)])
  else:
    print('Молодец! Верно..')
    break