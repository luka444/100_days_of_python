
students_height = input("Input list of student heights: ").split() # 

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])


total_height = 0

for height in students_height:
    total_height += height

# print(total_height)

num_of_students = 0

for student in students_height:
    num_of_students += 1

# print(num_of_students)

avarage = round((total_height / num_of_students),2)
print(f"Avarage height - {avarage}")