students = int(input())

students_grades = {}

for _ in range(students):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    grades_formatted = ' '.join(f"{g:.2f}" for g in grades)
    print(f"{student} -> {grades_formatted} (avg: {average_grade:.2f})")
