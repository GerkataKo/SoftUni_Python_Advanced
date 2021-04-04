def input_to_tuple():
    lines = tuple(char for char in input())

    return sorted(lines)


def count_chars(line):
    chars = {}
    for char in range(len(line)):
        if line[char] not in chars:
            chars[line[char]] = 0
        chars[line[char]] += 1
    return chars


def print_result(line):
    for char, count in count_chars(line).items():
        print(f"{char}: {count} time/s")


sorted_line = input_to_tuple()
print_result(sorted_line)
