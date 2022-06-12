WORKING = True

integer_part = ''
fractional_part = ''
number = ''


while WORKING:
    number = input('Введіть дрібне число: ')
    try:
        if float(number) and number[-1] == '.':
            if number[-1] == '.':
                number += '0'
            WORKING = False
    except ValueError:
        print(f'Ви ввели помилкові данні.')

integer_part, fractional_part = number.split('.')
print(f'Ціла частина числа: {integer_part}\n'
      f'Дрібна частина числа: {fractional_part}')
