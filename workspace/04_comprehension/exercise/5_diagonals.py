def read_matrix():
    size = int(input())
    matrix = [[int(x) for x in input().split(', ')] for i in range(size)]

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


def get_primary_diagonal(matrix):
    size = len(matrix)
    return ", ".join((str(matrix[_][_]) for _ in range(size)))


def get_secondary_diagonal(matrix):
    size = len(matrix)
    return ", ".join((str(matrix[_][size - _ - 1]) for _ in range(size)))


matrix = (read_matrix())
print(f"First diagonal: {get_primary_diagonal(matrix)}. Sum: {get_sum_of_primary_diagonal(matrix)}")
print(f"Second diagonal: {get_secondary_diagonal(matrix)}. Sum: {get_sum_of_secondary_diagonal(matrix)}")
