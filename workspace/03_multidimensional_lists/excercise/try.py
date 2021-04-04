def get_magic_triangle(n):
    trow = [1]
    y = [0]
    pascal_triangle = []
    pascal_triangle.append(trow)
    for x in range(n - 1):
        trow = [left + right for left, right in zip(trow + y, y + trow)]
        pascal_triangle.append(trow)
    return pascal_triangle


print(get_magic_triangle(5))