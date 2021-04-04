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


print(get_sum_of_primary_diagonal(read_matrix()))