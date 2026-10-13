#Write a Python program to count the number of digits in a positive integer using a while loop.

x=int(input("Enter Number :"))
y=0
while x>0:
  x = x // 10
  y = y + 1

print("Count positive integer :",y)



    
