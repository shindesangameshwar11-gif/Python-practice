#wap to print the numbers from 1 to 10 using while loop skip the number 5

x=1

while x<=10:
     if x==5:
      x= x + 1
      continue 

     print(x)
     x= x + 1

print("End of loop",x)