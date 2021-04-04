rows, columns = input().split(", ")
matrix=[]
sum_matrix = 0

for row in range(int(rows)):
    columns = input().split(",")
    nums_int = list(map(int, columns))
    matrix.append(nums_int)
    sum_matrix += sum(nums_int)

print(sum_matrix)
print(matrix)
