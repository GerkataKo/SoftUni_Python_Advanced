box = list(map(int, input().split(" ")))
rack_capacity = int(input())
rack_counters = 1
current_rack = 0

while box:
    cloth = box.pop()
    if (current_rack + cloth) > rack_capacity:
        rack_counters += 1
        box.append(cloth)
        current_rack=0
    else:
        current_rack+=cloth

print(rack_counters)
