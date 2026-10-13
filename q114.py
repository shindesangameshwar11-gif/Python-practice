#Write a Python program to repeatedly take numbers from the user until 0 is entered, then print their sum.

x=int(input("Enter a number :"))
y=0

while x != 0:
    y = y + x
    x=int(input("Enter a number :"))

print("sum of positive integer :",y)








