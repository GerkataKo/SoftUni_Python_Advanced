def avg(values):
    return sum(values) / len(values)

grades = int(input())
students_dict = {}

for i in range(grades):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(grade)

for key, values in students_dict.items():
        grades_string = ' '.join(f'{grade:.2f}' for grade in values)
        avg_grade = avg(values)
        print(f'{key} -> {grades_string} (avg: {avg_grade:.2f})')