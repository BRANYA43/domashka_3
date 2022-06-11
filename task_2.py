WORKING = True

integer_part = ''
fractional_part = ''
number = ''


while WORKING:
    number = input('Введіть дрібне число: ')
    try:
        if float(number) and not number.isdigit():
            if number[-1] == '.':
                number += '0'
            WORKING = False
    except ValueError:
        pass

integer_part, fractional_part = number.split('.')
print(f'Ціла частина числа: {integer_part}\n'
      f'Дрібна частина числа: {fractional_part}')
