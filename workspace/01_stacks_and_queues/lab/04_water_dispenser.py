from collections import deque

water_quantity = int(input())
start_cmd = "Start"
end_cmd = "End"

names = deque()
while True:
    name = input()
    if not name == start_cmd:
        names.append(name)
    else:
        break

while True:
    command = input()
    if command == end_cmd:
        print(f'{water_quantity} liters left')
        break
    elif command.startswith("refill"):
        command = command.split(' ')
        refill_liters = int(command[1])
        water_quantity += refill_liters
    else:
        person = names.popleft()
        person_litters = int(command)
        if person_litters <= water_quantity:
            print(f'{person} got water')
            water_quantity -= person_litters
        else:
            print(f'{person} must wait')
