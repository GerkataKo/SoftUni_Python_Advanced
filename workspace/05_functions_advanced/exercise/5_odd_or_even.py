def calculate(cmd, values):
    cmd_sum=0
    if cmd == "Odd":
        cmd_sum = sum([x for x in values if x % 2 != 0])
    elif cmd == "Even":
        cmd_sum = sum([x for x in values if x % 2 == 0])
    return cmd_sum*len(values)


command = input()
nums_list = [int(x) for x in input().split()]
result = calculate(command, nums_list)
print(result)