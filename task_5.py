from random import randint

count = 3
number = 0

guess_number = randint(1, 10)
print(guess_number)


def get_input_number(message: str):
    ret = ''
    while not ret.isdigit():
        ret = input(message)

    return int(ret)


while count > 0:
    number = get_input_number('Введіть число від 1 до 10: ')
    if 0 < number < 11:

        if guess_number == number and count != 0:
            print(f'Вітаємо, Ви вгадали!')
            break
        else:
            print('Ви не вгадали.')
            print('*' * 20)
            count -= 1

        if count == 0:
            print('У вас не залишилось спроб.')
        elif count == 1:
            print(f'Залишлось {count} спроба.')
        elif 2 <= count <= 4:
            print(f'Залишилось {count} спроби.')
        elif count >= 5:
            print(f'Залишилось {count} спроб.')
    else:
        print('Ви ввели число вне діпазону.')
        print('*' * 20)
