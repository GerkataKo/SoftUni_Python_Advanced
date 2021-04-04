def get_letter(value):
    char = "a"
    return chr(ord(char)+value)

def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for r in range(rows_count):
        matrix.append([])
        for c in range(columns_count):
            matrix[r].append(f"{get_letter(r)}{get_letter(r+c)}{get_letter(r)}")
    return matrix

def print_result(matrix):
    for r in range(len(matrix)):
        print(' '.join(s for s in matrix[r]))

print_result(read_matrix())