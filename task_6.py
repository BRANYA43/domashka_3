from random import randint

X_AXIS = tuple(range(1, 9))
Y_AXIS = tuple(chr(elem) for elem in range(ord('A'), ord('A') + 8))
DICT_DIRECTION = {'up': '1', 'down': '2', 'left': '3', 'right': '4'}

x_rand = randint(0, len(X_AXIS) - 1)
y_rand = randint(0, len(Y_AXIS) - 1)

knight = {'x': X_AXIS[x_rand], 'y': Y_AXIS[y_rand]}
save_knight = knight.copy()

all_possible_moves = []
cords_moves = []


def get_two_random_cords(cords_moves):
    for i in range(2):
        x = randint(0, len(X_AXIS) - 1)
        y = randint(0, len(Y_AXIS) - 1)
        cords_moves.append((X_AXIS[x], Y_AXIS[y]))


def add_cords(list_for_cords: list, piece: dict, save_piece: dict):
    if X_AXIS.index(save_piece['x']) - 3 < X_AXIS.index(piece['x']) < X_AXIS.index(save_piece['x']) + 3 \
            and Y_AXIS.index(save_piece['y']) - 3 < Y_AXIS.index(piece['y']) < Y_AXIS.index(save_piece['y']) + 3:
        list_for_cords.append((piece['x'], piece['y']))


def set_cord_move(direction: str, piece: dict, distance_move: int):
    global DICT_DIRECTION, X_AXIS, Y_AXIS
    x = X_AXIS.index(piece['x'])
    y = Y_AXIS.index(piece['y'])

    if direction == DICT_DIRECTION['up']:
        piece['y'] = Y_AXIS[y - distance_move]
    elif direction == DICT_DIRECTION['down']:
        piece['y'] = Y_AXIS[y + distance_move]

    elif direction == DICT_DIRECTION['left']:
        piece['x'] = X_AXIS[x - distance_move]
    elif direction == DICT_DIRECTION['right']:
        piece['x'] = X_AXIS[x + distance_move]


def get_two_next_direction(direction: str):
    directions_move = []
    if direction == DICT_DIRECTION['up'] or direction == DICT_DIRECTION['down']:
        directions_move.append(DICT_DIRECTION['left'])
        directions_move.append(DICT_DIRECTION['right'])

    elif direction == DICT_DIRECTION['left'] or direction == DICT_DIRECTION['right']:
        directions_move.append(DICT_DIRECTION['up'])
        directions_move.append(DICT_DIRECTION['down'])

    return directions_move


for key in DICT_DIRECTION:
    direction_1 = DICT_DIRECTION[key]
    two_next_direction = get_two_next_direction(direction_1)
    for direction_2 in two_next_direction:
        try:
            set_cord_move(direction_1, knight, distance_move=2)
            set_cord_move(direction_2, knight, distance_move=1)
            add_cords(all_possible_moves, knight, save_knight)
        except IndexError:
            pass

        knight = save_knight.copy()

get_two_random_cords(cords_moves)

for i in cords_moves:
    for j in all_possible_moves:
        if i == j:
            print('+')

print(all_possible_moves)
print(save_knight)
print(cords_moves)
