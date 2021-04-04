def strs_to_ints(strs):
    return [int(x) for x in strs]

def read_line():
    return strs_to_ints(input().split(', '))

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x >= 0

def get_even(values):
    return [x for x in values if is_even(x)]

def get_odd(values):
    return [x for x in values if not is_even(x)]

def get_positive(values):
    return [x for x in values if is_positive(x)]

def get_negative(values):
    return [x for x in values if not is_positive(x)]

def print_result(values):
    return (", ".join((str(value) for value in values)))

nums=read_line()
positive_nums=get_positive(nums)
negative_nums=get_negative(nums)
even_nums=get_even(nums)
odd_nums=get_odd(nums)
print(f"Positive: {print_result(positive_nums)}")
print(f"Negative: {print_result(negative_nums)}")
print(f"Even: {print_result(even_nums)}")
print(f"Odd: {print_result(odd_nums)}")