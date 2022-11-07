# МОДУЛЬ 2
# bornyear.py
def bornyear():
  right_pushkin_birthday = 1799
  input_pushkin_birthday = int(input('Введите год рождения Саши Пушкина?: '))
  if input_pushkin_birthday != right_pushkin_birthday:
    print('Неверно!')
  else:
    print('Верно!')
  pass

if __name__ == '__main__':
  bornyear()