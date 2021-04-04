def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input().split()]
        matrix.append(row)
    return matrix


def get_player_position(matrix, size):
    player_pos=[]
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'P':
                player_pos = [r, c]
                break
    return player_pos


def is_valid_coordinates(value, max_value):
    if 0 <= value < max_value:
        return True
    else:
        return False


def get_player_moves(size, matrix, player_pos):
    player_row = player_pos[0]
    player_col = player_pos[1]
    coins_collected = 0
    game_over = False
    player_moves = []
    while True:
        command = input()
        if command == '':
            break
        elif command == 'up':
            player_row -= 1
            if is_valid_coordinates(player_row, size):
                if matrix[player_row][player_col] == 'X':
                    game_over = True
                else:
                    coins_collected += int(matrix[player_row][player_col])
                    player_moves.append([player_row, player_col])
            else:
                game_over = True

        elif command == 'down':
            player_row += 1
            if is_valid_coordinates(player_row, size):
                if matrix[player_row][player_col] == 'X':
                    game_over = True
                else:
                    coins_collected += int(matrix[player_row][player_col])
                    player_moves.append([player_row, player_col])
            else:
                game_over = True

        elif command == 'left':
            player_col -= 1
            if is_valid_coordinates(player_col, size):
                if matrix[player_row][player_col] == 'X':
                    game_over = True
                else:
                    coins_collected += int(matrix[player_row][player_col])
                    player_moves.append([player_row, player_col])
            else:
                game_over = True

        elif command == 'right':
            player_col += 1
            if is_valid_coordinates(player_col, size):
                if matrix[player_row][player_col] == 'X':
                    game_over = True
                else:
                    coins_collected += int(matrix[player_row][player_col])
                    player_moves.append([player_row, player_col])
            else:
                game_over = True

        else:
            continue

        if game_over or coins_collected >= 100:
            break

    return matrix, coins_collected, player_moves, game_over


def print_result(game_over, player_moves, coins_collected):
    if not game_over:
        print(f'You won! You\'ve collected {coins_collected} coins.')
    else:
        print(f'Game over! You\'ve collected {int(coins_collected // 2)} coins.')
    print('Your path:')
    for move in player_moves:
        print(move)


size = int(input())
field = read_matrix(size)
player_pos = get_player_position(field, size)
matrix, coins_collected, player_moves, game_over = get_player_moves(size, field, player_pos)
print_result(game_over, player_moves, coins_collected)