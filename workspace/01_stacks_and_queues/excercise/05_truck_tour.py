from collections import deque

n = int(input())
pumps = deque(input() for i in range(n))

for big in range(n):
    is_valid = True
    tank = 0
    for small in range(n):
        current_pump = pumps[small]
        petrol, distance = current_pump.split()
        petrol = int(petrol)
        distance = int(distance)
        tank += petrol - distance

        if tank < 0:
            is_valid = False
            pumps.append(pumps.popleft())
            break
    if is_valid:
        print(big)
        break
