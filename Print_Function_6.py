# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:
# 123....n

def number(n):
    for i in range(1,n+1):
        print(i, end="")

n=int(input())
number(n)

       