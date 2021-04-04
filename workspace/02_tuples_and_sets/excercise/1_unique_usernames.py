def input_to_set(count):
    lines = set()
    for _ in range(count):
        lines.add(input())

    return lines


def print_result(names):
    for name in names:
        print(name)


n = int(input())
names = input_to_set(n)
print_result(names)
