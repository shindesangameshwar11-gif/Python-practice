#wap to count a number of positive integer

num= int(input("Enter a number :"))
c=0

while num >0:
    num= num // 10
    c = c + 1

print("Number of digits :",c)