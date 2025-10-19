# Problem Description*******

# You are a shoe shop owner. Your shop has a certain number of shoes, and each shoe has a size.

# There are customers who want to buy shoes. Each customer will buy only if a shoe of their desired size is available. They also offer a price they are willing to pay for that shoe.

# Your task is to calculate the total money earned after serving all customers.

# Input Format*******

# The first line contains an integer, n → the number of shoes in the shop.

# The second line contains n space-separated integers → the sizes of the shoes in the shop.

# The third line contains an integer, x → the number of customers.

# The next x lines each contain two space-separated integers:

# size → the size of shoe the customer wants

# price → the amount the customer will pay if they get the shoe

print("Enter total number of shoe")
shoe=int(input())

print("Enter available shoe size")
size=input().split()
for i in range(len(size)):
    size[i]=int(size[i])

print("Enter total customer")
customer=int(input())

total_sell=0

print("Enter your shoe size and price")
for _ in range(customer):
    data=input().split()
    shoe_size=int(data[0])
    price=int(data[1])

    if shoe_size in size:
        total_sell+=price
        size.remove(shoe_size)
print(total_sell)



