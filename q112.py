#Write a Python program to calculate the sum of all digits of a positive integer using a while loop.

s=int(input("Enter Number :"))
o=0

while s>0:
    q = s % 10
    o = o + q
    s = s // 10

print("sum of digits :",o)



