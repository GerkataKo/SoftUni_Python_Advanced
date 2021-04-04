def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)

    return matrix


def get_sum_of_primary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def get_sum_of_secondary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    return diagonal_sum

matrix=read_matrix()

print(abs(get_sum_of_primary_diagonal(matrix)-get_sum_of_secondary_diagonal(matrix)))
