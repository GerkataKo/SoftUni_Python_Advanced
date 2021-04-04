def read_matrix():
    lists = input().split('|')
    return [lists[_].split() for _ in range(len(lists))[::-1]]


matrix = read_matrix()
result = [int(x) for row in matrix for x in row]
print(*result)
