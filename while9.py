#Wap to reverse a positive integer

num=int(input("Enter a Number :"))
rev=0

while num>0:
    digit= num % 10
    rev = rev * 10 + digit
    num= num // 10

print("Reverse Number :",rev)