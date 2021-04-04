numbers=tuple(map(float, input().split()))

nums_occurrences={}
for num in numbers:
    if num not in nums_occurrences:
        nums_occurrences[num]=0
    nums_occurrences[num] +=1

[print(f"{key} - {value} times") for key,value in nums_occurrences.items()]
