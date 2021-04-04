nums_list=[int(x) for x in input().split()]
print(list(filter(lambda x: x%2==0, nums_list)))