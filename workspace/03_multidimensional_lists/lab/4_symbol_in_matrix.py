def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        matrix.append([char for char in input()])

    return matrix


def find_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if symbol == matrix[row][column]:
                return row, column
    return f"{symbol} does not occur in the matrix"


matrix = read_matrix()
symbol = input()

print(find_symbol(matrix, symbol))