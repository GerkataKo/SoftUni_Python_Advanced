def input_to_set(input_line):
    lines = set()
    for _ in range(len(input_line)):
        lines.add(input_line[_])

    return lines


def print_result(elements):
    for element in elements:
        print(element)


num = int(input())
elements = set()

for i in range(num):
    line = input().split()
    elements|=(input_to_set(line))

print_result(elements)
