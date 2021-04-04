def get_heroes_items(values):
    cmd = input()
    while cmd!="End":
        name, inventory, cost=cmd.split("-")
        cost=int(cost)
        if name in values:
            if inventory not in values[name]:
                values[name][inventory]=cost
        else:
            values[name]={inventory:cost}
        cmd=input()
    return values

def print_result (values):
    for name, value in values.items():
        count_items = 0
        sum_cost = 0
        for item, cost in value.items():
            count_items += 1
            sum_cost += cost
        print(f'{name} -> Items: {count_items}, Cost: {sum_cost}')

names ={name: {} for name in input().split(', ')}
inventory=get_heroes_items(names)
print_result(inventory)