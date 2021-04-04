def read_matrix():
    rows_counts = int(input())
    return [input().split(', ') for _ in range(rows_counts)]

matrix = read_matrix()
result = [int(x) for row in matrix for x in row]
print(result)