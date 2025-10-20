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
    