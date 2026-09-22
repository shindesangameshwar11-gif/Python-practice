#wap to print numbers 1 to 20 skip even numbers

x=1

while x<=20:
    if x // 100:
       x = x + 2
       continue

    print(x)
    x = x + 2

print(x)