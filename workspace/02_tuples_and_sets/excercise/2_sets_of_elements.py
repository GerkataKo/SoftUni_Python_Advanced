def input_to_set(str):
    count = int(str)
    lines = set()
    for _ in range(count):
        lines.add(input())

    return lines


def print_result(elements):
    for element in elements:
        print(element)


n, m = input().split()

n_set = input_to_set(n)
m_set = (input_to_set(m))

unique_elements_set = n_set.intersection(m_set)

print_result(unique_elements_set)
