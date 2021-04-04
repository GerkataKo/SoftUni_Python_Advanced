def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = input().split()
        matrix.append(row)

    return matrix


def check_command(line, matrix):
    if "swap" in line:
        coordinates = line.split()[1:]
        if len(coordinates) == 4:
            coordinates = list(map(int, coordinates))
            if coordinates[0] in range(len(matrix)) and coordinates[2] in range(len(matrix)):
                if coordinates[1] in range(len(matrix[0])) and coordinates[3] in range(len(matrix[0])):
                    return swap_matrix(matrix, coordinates)
    return False


def swap_matrix(matrix, coordinates):
    row1, col1, row2, col2 = coordinates
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def print_result(matrix):
    for r in range(len(matrix)):
        print(' '.join(s for s in matrix[r]))


matrix = read_matrix()
command = input()

while command != "END":
    command = check_command(command, matrix)
    if not command:
        print("Invalid input!")
    else:
        print_result(command)
    command = input()
