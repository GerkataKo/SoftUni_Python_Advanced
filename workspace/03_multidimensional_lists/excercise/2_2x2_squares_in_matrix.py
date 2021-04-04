def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [x for x in input().split()]
        matrix.append(row)

    return matrix


def is_match(matrix, row_index, column_index, size):
    counter = 0
    char = matrix[row_index][column_index]
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            if char == matrix[r][c]:
                counter += 1
    if counter == 4:
        return True
    else:
        return False


def count_squares(matrix, square_size):
    counter = 0
    for row_index in range(len(matrix) - square_size + 1):
        for col_index in range(len(matrix[row_index]) - square_size + 1):
            if is_match(matrix, row_index, col_index, square_size):
                counter += 1

    return counter


SQUARE_SIZE = 2
matrix = read_matrix()

print(count_squares(matrix, SQUARE_SIZE))
