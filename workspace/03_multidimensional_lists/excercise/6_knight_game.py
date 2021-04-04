n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))


def is_valid(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def count_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        p_row = row + rows[index]
        p_col = col + cols[index]
        if is_valid(p_row, p_col):
            p_position = matrix[p_row][p_col]
            if p_position == "K":
                kills += 1

    return kills


removed_counter = 0
while True:
    max_kills = 0
    killer_position = []
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == "K":
                kills = count_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]
    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = "0"
        removed_counter += 1
    else:
        break

print(removed_counter)
