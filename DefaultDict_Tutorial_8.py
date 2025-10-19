

# Input Format

# The first line contains integers, n and m  separated by a space.
# The next n lines contains the words belonging to group A .
# The next m lines contains the words belonging to group B.


value=input().split()
n=int(value[0])
m=int(value[1])


group_A=[]
for _ in range(n):
    word=input().strip()
    group_A.append(word)



group_B=[]
for _ in range(m):
    word=input().strip()
    group_B.append(word)

for word in group_B:
    position=[]
    for i in range(len(group_A)):
        if group_A[i]==word:
            position.append(i+1)
print(*position)
