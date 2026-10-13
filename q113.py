#Write a Python program to reverse a positive integer using a while loop.

a=int(input("Enter Number :"))
b=0

while a>0:
    c = a % 10
    b = b * 10 + c
    a = a // 10

print("Reversed positive integer :",b)





