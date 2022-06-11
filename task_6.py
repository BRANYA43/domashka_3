X_AXIS = tuple(range(1, 9))
Y_AXIS = tuple(chr(elem) for elem in range(ord('A'), ord('A') + 9))
DICT_DIRECTION  = {'up': '1', 'down': '2', 'left': '3', 'right': '4'}

knight = {'x': X_AXIS[4], 'y': Y_AXIS[4]}
save_start_cords = knight

all_possible_moves = []


def set_cord_move(direction: str, piece: dict, distance_move):
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


def get_cords_move(direction_1: str, piece: dict):
    set_cord_move(direction_1, piece, distance_move=2)
    cords = (piece['x'], piece['y'])
    return cords


def get_two_next_direction(direction: str, index: int):
    directions_move = []
    if direction == DICT_DIRECTION['up'] or direction == DICT_DIRECTION['down']:
        directions_move.append(DICT_DIRECTION['left'])
        directions_move.append(DICT_DIRECTION['right'])

    elif direction == DICT_DIRECTION['left'] or direction == DICT_DIRECTION['right']:
        directions_move.append(DICT_DIRECTION['up'])
        directions_move.append(DICT_DIRECTION['down'])

    return directions_move[index]

for key in DICT_DIRECTION.keys():
    pass