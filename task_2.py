integer_part = ''
fractional_part = ''
number = ''

number = input('Введіть дрібне число: ')

integer_part, fractional_part = number.split('.')
print(f'Ціла частина числа: {integer_part}\n'
      f'Дрібна частина числа: {fractional_part}')