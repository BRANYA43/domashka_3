X_AXIS = tuple(range(1, 9))
Y_AXIS = tuple(chr(elem) for elem in range(ord('A'), ord('A') + 8))
DICT_DIRECTION = {'up': '1', 'down': '2', 'left': '3', 'right': '4'}

knight = {'x': X_AXIS[4], 'y': Y_AXIS[0]}
save_knight = knight.copy()

all_possible_move = []


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
            if X_AXIS.index(save_knight['x']) - 3 < X_AXIS.index(knight['x']) < X_AXIS.index(save_knight['x']) + 3 \
                and Y_AXIS.index(save_knight['y']) - 3 < Y_AXIS.index(knight['y']) < Y_AXIS.index(save_knight['y']) + 3:

                all_possible_move.append((knight['x'], knight['y']))
        except IndexError:
            pass


        knight = save_knight.copy()
print(all_possible_move)
print(save_knight)
