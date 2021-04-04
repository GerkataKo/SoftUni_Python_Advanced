from collections import deque

names = deque()

paid_cmd = "Paid"
end_cmd = "End"

while True:
    name = input()
    if name == end_cmd:
        print(f'{len(names)} people remaining.')
        break
    elif name == paid_cmd:
        while names:
            print(names.popleft())
    else:
        names.append(name)
