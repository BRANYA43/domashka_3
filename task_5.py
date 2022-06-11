from random import randint


count = 0
MAX_COUNT = 3
guess_number = randint(1, 10)
number = int(input('Введіть число: '))

if guess_number == number and count != MAX_COUNT:
    print('Вы вгадали')
else:
    print('Вы не вгадали')