def sum_name(name, line):
    sum = 0
    for char in name:
        sum += ord(char)
    sum //= line
    return sum


def set_creation(num):
    odd = set()
    even = set()
    for i in range(1, num + 1):
        sum = sum_name(input(), i)
        if sum % 2 == 0:
            even.add(sum)
        else:
            odd.add(sum)
    return odd, even


n = int(input())
odd_set, even_set = set_creation(n)

if sum(odd_set) == sum(even_set):
    print(str(odd_set | even_set)[1:-1])
elif sum(odd_set) > sum(even_set):
    print(str(odd_set - even_set)[1:-1])
else:
    print(str(odd_set ^ even_set)[1:-1])
