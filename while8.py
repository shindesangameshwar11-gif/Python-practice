#wap to calculate the sum of all digits positive integer

a=int(input("Enter a Number :"))
b=0

while a>0:
    c= a % 10
    b = b + c
    a = a // 10

print("Sum of digits :",b)