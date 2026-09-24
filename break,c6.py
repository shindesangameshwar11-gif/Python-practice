#wap to print numbers from 1 to 20 but skip that numbers divisible by 3

a=1

while a<=20:
    if a // 100:
       a += 1
       continue
 
    a += 2
    print(a)

print(a)