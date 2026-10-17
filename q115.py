#Write a Python program to print numbers from 1 to 10 and stop the loop when the number becomes 6 using break.

x=0
while x<=10:
    print(x)
    x+=1
    if x==6:
        break
print(x)