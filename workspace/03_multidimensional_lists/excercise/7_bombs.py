def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix


def is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def blow_bomb(matrix, number):
    rows = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for index in range(len(rows)):
        blown_row = r + rows[index]
        blown_col = c + cols[index]
        if is_valid(blown_row, blown_col, len(matrix)):
            if matrix[blown_row][blown_col] > 0:
                matrix[blown_row][blown_col] = matrix[blown_row][blown_col] - bomb


def active_cells(matrix):
    active_cells = []
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] > 0:
                active_cells.append(matrix[r][c])
    return active_cells


def print_result(matrix):
    for r in range(len(matrix)):
        print(' '.join(str(s) for s in matrix[r]))


matrix = read_matrix()
coordinates = input().split()
bomb = 0

for index in range(len(coordinates)):
    row_index, col_index = map(int, coordinates[index].split(","))
    if matrix[row_index][col_index] < 0:
        bomb = 0
    else:
        bomb = matrix[row_index][col_index]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r == row_index and c == col_index:
                blow_bomb(matrix, bomb)

count = len(active_cells(matrix))
sum = sum(active_cells(matrix))

print(f"Alive cells: {count}")
print(f"Sum: {sum}")
print_result(matrix)
