def get_integral(number: int):
    if number == 1:
        return 1
    else:
        return number * get_integral(number - 1)


number = int(input('Введіть число: '))

print(get_integral(number))
