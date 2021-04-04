def set_creation(string):
    nums = set()
    start, finish = string.split(",")
    for i in range(int(start), int(finish) + 1):
        nums.add(i)
    return nums


n = int(input())
longest_intersection = set()

for i in range(n):
    line = input().split("-")
    set_1 = set_creation(line[0])
    set_2 = set_creation(line[1])
    intersected_set = set_1.intersection(set_2)
    if len(intersected_set) > len(longest_intersection):
        longest_intersection = intersected_set

print(f"Longest intersection is [{str(longest_intersection)[1:-1]}] with length {len(longest_intersection)}")
