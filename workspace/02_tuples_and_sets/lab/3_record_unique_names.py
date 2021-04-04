def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines

n=int(input())
names=input_to_list(n)

unique_names=set(names)
[print(name) for name in unique_names]