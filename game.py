from input_output import input_coordinates, print_field


field = [[None, None, None], [None, None, None], [None, None, None]]
players = ["x", "o"]

for turn in range(9):
    player = players[turn % 2]

    x, y = input_coordinates(field, player)
    field[y][x] = player

    # check_for_win()

    print_field(field)
