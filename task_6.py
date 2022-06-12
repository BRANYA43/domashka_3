from random import randint

X_AXIS = tuple(str(elem) for elem in range(1, 9))
Y_AXIS = tuple(chr(elem) for elem in range(ord('A'), ord('A') + 8))

knight = {'x': 0, 'y': 0}

list_coordinates = []

count = 0


def add_coordinates_in_list(list_coordinates: list, x: int, y: int):
    list_coordinates.append({'x': x, 'y': y})


def print_list_axis(axis):
    for i, elem in enumerate(axis):
        print(f'{i}. {elem}')


def get_input_digit(message: str):
    ret = ''
    while not ret.isdigit():
        try:
            ret = input(message)
        except ValueError:
            pass
    return int(ret)


def check_possible_move(coordinates: dict, knight: dict):
    x = abs(coordinates['x'] - knight['x'])
    y = abs(coordinates['y'] - knight['y'])

    if x == 2 and y == 1 or x == 1 and y == 2:
        print(f'Кінь с ({X_AXIS[knight["x"]]} {Y_AXIS[knight["y"]]}) може походить на'
              f' ({X_AXIS[coordinates["x"]]} {Y_AXIS[coordinates["y"]]}).')
    else:
        print(f'Кінь с ({X_AXIS[knight["x"]]} {Y_AXIS[knight["y"]]}) не може походить на'
              f' ({X_AXIS[coordinates["x"]]} {Y_AXIS[coordinates["y"]]}).')


input('Введіть координати для фігури Коня.\n'
      '(Натисніть Enter щоб продовжити)')
print_list_axis(X_AXIS)
knight['x'] = get_input_digit('Введіть координату X: ')
print_list_axis(Y_AXIS)
knight['y'] = get_input_digit('Введіть координату Y: ')

while 1 > count or count > 64:
    count = get_input_digit('Введіть кільсть позицій від 1 до 64: ')

for i in range(count):
    add_coordinates_in_list(list_coordinates,
                            randint(0, len(X_AXIS) - 1),
                            randint(0, len(Y_AXIS) - 1))


for elem in list_coordinates:
    check_possible_move(elem, knight)
