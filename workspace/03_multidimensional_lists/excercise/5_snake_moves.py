from collections import deque


def print_result(matrix):
    for r in range(len(matrix)):
        print(''.join(s for s in matrix[r]))


(rows, columns) = map(int, input().split())
snake = deque(input())

matrix = []

for r in range(rows):
    matrix.append(deque())
    for c in range(columns):
        filler = snake.popleft()
        if r % 2 == 0:
            matrix[r].append(filler)
        elif r % 2 != 0:
            matrix[r].appendleft(filler)
        snake.append(filler)

print_result(matrix)
