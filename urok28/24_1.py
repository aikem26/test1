# №1
from hw import students

#print(students)
male_count = 0
female_count = 0
for element in students:
    g = element["gender"]
    if g == "Male":
        male_count += 1
    elif g == "Female":
        female_count += 1

male_percent = round((male_count * 100) / len(students), 2)
female_percent = round((female_count * 100) / len(students), 2)

print(male_count, female_count)
print("Процент мужчин:", male_percent)
print("Процент женщин:",female_percent)

# №2
python_students = [element["name"] for element in students if element["course"] == "python"]
print(python_students)

# №3
#for student in students:
    #for another_student in students:
        #if student == another_student:
            #print(student, another_student)

unique_students = []

for student in students:
    if student not in unique_students:
        unique_students.append(student)

print(unique_students)

#for i in range(len(students)):
    #student = students[i]
    #for j in range(i + 1, len(students)):
        #another_student = students[j]
        #if student == another_student:
            #print(i, student["name"], j, another_student["name"])

for i, student in enumerate(students):
    for j, another_student in enumerate(students[i+1:]):
        if student == another_student:
            print(i, student["name"], j, another_student["name"])

#4
students_1 = [student["name"] for student in students if student["age"] > 30]
print(students_1)
print(round(len(students_1) * 100 / len(students)))

#6
for student in students:
    if student["course"] == "javascript":
        student["course"] == "python"

print(students)

#7
student_1 = {
    'name': 'Aike',
    'age': 24,
    'course': 'python',
    'gender': 'Female'
}

student_2 = {
    'name': 'Burul',
    'age': 23,
    'course': 'python',
    'gender': 'Female'
}

student_3 = {
    'name': 'Asel',
    'age': 45,
    'course': 'java',
    'gender': 'Female'
}

student_4 = {
    'name': 'Alinur',
    'age': 18,
    'course': 'java',
    'gender': 'Male'
}


student_5 = {
    'name': 'Alisher',
    'age': 17,
    'course': 'python',
    'gender': 'Male'
}


student_6 = {
    'name': 'Ulan',
    'age': 29,
    'course': 'java',
    'gender': 'Male'
}


student_7 = {
    'name': 'Meka',
    'age': 26,
    'course': 'java',
    'gender': 'Female'
}


student_8 = {
    'name': 'Musa',
    'age': 54,
    'course': 'java',
    'gender': 'Male'
}


student_9 = {
    'name': 'Ailin',
    'age': 20,
    'course': 'python',
    'gender': 'Female'
}


student_10 = {
    'name': 'Seit',
    'age': 25,
    'course': 'python',
    'gender': 'Male'
}

students.append(student_1)
students.append(student_2)
students.append(student_3)
students.append(student_4)
students.append(student_5)
students.append(student_6)
students.append(student_7)
students.append(student_8)
students.append(student_9)
students.append(student_10)

#8
new_students = [student for student in students if not student["age"] < 15]
print(new_students)
