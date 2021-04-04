from collections import deque


def stock_availability(inventory_list, command, *args):
    inventory = deque(inventory_list)
    if command == "delivery":
        inventory = delivery(inventory, *args)
    elif command == "sell":
        inventory = sell(inventory, *args)
    return list(inventory)


def delivery(deque_list, *args):
    for box in args:
        deque_list.append(box)
    return deque_list


def sell(deque_list, *args):
    if not args and deque_list:
        deque_list.popleft()
    else:
        for item in args:
            if type(item)==int:
                for i in range(item):
                    deque_list.popleft()
                    if not deque_list:
                        deque_list = []
                        break
            elif type(item) is str:
                for box in args:
                    if box in deque_list:
                        deque_list = deque(filter(lambda a: a != box, deque_list))
    return deque_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell","chocolate",2))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

