# Input Format
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the mark,id ,name  and class, under their respective column names.

from collections import namedtuple

N=int(input())
field=input().split()
student=namedtuple('student',field)

total=0
for _ in range(N):
    data=input().split()
    student1=student(*data)
    total+=int(student1.mark)

print(f"{total:.2f}")



# Task:
# You are given student data with Name, ID, CLASS, and MARKS in random column order.
# Your task is to find the student who scored the highest MARKS and print

from collections import namedtuple

N = int(input())
fields = input().split()  # column names

Student = namedtuple('Student', fields)

top_name = ""
top_marks = -1

for _ in range(N):
    data = input().split()
    person = Student(*data)
    
    if int(person.MARKS) > top_marks:
        top_marks = int(person.MARKS)
        top_name = person.NAME

print(top_name, top_marks)



# You are given student data.

# First line contains N → number of students.

# Second line contains column names (for example: ID NAME CLASS MARKS) — order can be random.

# Next N lines contain each student’s data in the same order as the column names.

# Task:
# Print the NAME and MARKS of the student who scored the highest MARKS.
N = int(input())
fields = input().split()

students = []
for _ in range(N):
    data = input().split()
    student = dict(zip(fields, data))  # Create key:value dictionary
    students.append(student)

top_student = max(students, key=lambda x: int(x["MARKS"]))

print(top_student["NAME"], top_student["MARKS"])
