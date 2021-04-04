def get_data(string):
    _, data = string.split(":")
    data = int(data)
    return data


def get_bunker_items(values):
    total_quantity = 0
    total_quality = 0
    n = int(input())
    for i in range(n):
        line = input().split(" - ")
        if line[0] not in values:
            values[line[0]] = []
        values[line[0]].append(line[1])

        data = line[2].split(";")
        quantity = get_data(data[0])
        quality = get_data(data[1])
        total_quantity += quantity
        total_quality += quality

    return values, total_quantity, total_quality


def print_result(values):
    for category, value in values.items():
        print(f'{category} -> {", ".join(item for item in value)}')


categories = {category: [] for category in input().split(', ')}
inventory, quantity, quality = get_bunker_items(categories)
average_quality = quality / len(categories)
print(f"Count of items: {quantity}")
print(f"Average quality: {average_quality:.2f}")
print_result(inventory)
