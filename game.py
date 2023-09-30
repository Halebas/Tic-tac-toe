field = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
players = ["x", "o"]

for turn in range(9):
    player = players[turn % 2]

    x, y = map(int, input(f'Input coordinates for "{player}": ').split())

    if 0 <= x <= 2 and 0 <= y <= 2:
        if field[y][x] == ".":
            field[y][x] = player
        else:
            print("wrong input")
    else:
        print("wrong input")

    # check_for_win()

    print(field)
