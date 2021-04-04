def find_start_coordinates(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "s":
                return r, c


def count_coal(matrix):
    counter = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "c":
                counter += 1
    return counter


n = int(input())
commands = input().split(" ")

field = []
for _ in range(n):
    field.append(input().split())

start_row, start_col = find_start_coordinates(field)
counter_coal = count_coal(field)

no_more_commands = True

for i in range(len(commands)):
    command = commands[i]
    # Up command
    if command == 'up' and start_row - 1 in range(n):
        start_row -= 1
    # Down command
    elif command == 'down' and start_row + 1 in range(n):
        start_row += 1
    # Left command
    elif command == 'left' and start_col - 1 in range(n):
        start_col -= 1
    # Right command
    elif command == 'right' and start_col + 1 in range(n):
        start_col += 1

    if field[start_row][start_col] == "c":
        field[start_row][start_col] = "*"
        counter_coal -= 1
        if counter_coal == 0:
            print(f"You collected all coals! ({start_row}, {start_col})")
            no_more_commands = False
            break
    if field[start_row][start_col] == "e":
        print(f"Game over! ({start_row}, {start_col})")
        no_more_commands = False
        break

if no_more_commands:
    print(f"{counter_coal} coals left. ({start_row}, {start_col})")
