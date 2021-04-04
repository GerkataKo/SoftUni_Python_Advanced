def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(parking_lot):
    if parking_lot:
        for car in parking_lot:
            print(car)
    else:
        print('Parking Lot is Empty')


n = int(input())
cars = input_to_list(n)

parking_lot = set()

for vehicle in cars:
    command, car = vehicle.split(', ')
    if command == 'IN':
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

print_result(parking_lot)

