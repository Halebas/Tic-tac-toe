def input_coordinates(field, player: str):
    x, y = map(int, input(f'Input coordinates for "{player}": ').split())

    while x < 0 or x > 2 or y < 0 or y > 2 or field[y][x]:
        print("Wrong input!!!")
        x, y = map(int, input(f'Input coordinates for "{player}": ').split())

    return (x, y)


def print_field(field):
    print(field)
