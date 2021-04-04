from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split(" ")))

print(max(orders))

while orders and orders[0] <= food_quantity:
    food_quantity -= orders.popleft()

if not orders:
    print("Orders complete")
else:
    print("Orders left:", *orders)
