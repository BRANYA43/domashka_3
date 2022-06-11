number = ''

while not number.isdigit():
    number = input('Введіть трьохзначне число: ')
    if len(number) != 3:
        number = ''

digits = [int(element) for element in number]
print(f'Cумма цифр числа {number} дорінює {sum(digits)}')
