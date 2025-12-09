
n = int(input())


all_grades = []
good_behavior_students = []


for _ in range(n):
    line = input().strip()
    parts = line.split()

    name = parts[0]
    grade = float(parts[1])
    behavior = parts[2]


    all_grades.append(grade)


    if behavior == "добро":
        good_behavior_students.append((name, grade))5


avg_grade = sum(all_grades) / len(all_grades)
print(f"Среден успех на класа: {avg_grade:.2f}")


above_550 = sum(1 for g in all_grades if g > 5.50)
print(f"Ученици над 5.50: {above_550}")


below_350 = sum(1 for g in all_grades if g < 3.50)
print(f"Ученици под 3.50: {below_350}")


if good_behavior_students:

    good_behavior_students.sort(key=lambda x: x[1], reverse=True)

    print("Добро поведение (сортирани):")
    for name, grade in good_behavior_students:

        print(f"{name} - {grade:.1f}")
else:
    print("Няма ученици с добро поведение.")