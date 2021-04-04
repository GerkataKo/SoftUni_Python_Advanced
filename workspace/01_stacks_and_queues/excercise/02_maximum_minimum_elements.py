elements = []
max_number = 0
min_number = 0

queries = int(input())

for i in range(1, queries + 1):
    query = input().split()
    cmd = query[0]
    if cmd == "1":
        number = int(query[1])
        elements.append(number)
        if len(elements) > 1:
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number
        else:
            max_number = number
            min_number = number
    if cmd == "2" and len(elements) > 0:
        pop = elements.pop()
        if pop == min_number and len(elements) != 0:
            min_number = elements[len(elements) - 1]
        if pop == max_number and len(elements) != 0:
            max_number = elements[len(elements) - 1]
    if cmd == "3" and len(elements) > 0:
        print(max_number)
    if cmd == "4" and len(elements) > 0:
        print(min_number)

print(', '.join(map(str, reversed(elements))))
