from collections import deque

kids = input().split()
tosses = int(input())

hot_potato=deque(kids)

while len(hot_potato) > 1:
    hot_potato.rotate(-tosses + 1)
    print(f'Removed {hot_potato.popleft()}')

print(f'Last is {hot_potato.popleft()}')
