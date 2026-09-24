#wap that repeats asks theuser to enter a number perform the following operation
#if number is negative skip
#if number is 0 stop the loop
#add all positive numbers to a total.
#after the loop end print the total of all positive numbers entered

y=0
while True:

    x=int(input("Enter a number :"))

    if(x<0):
        continue

    elif(x==0):
        break

    y = x + y 
    

    print("You entered :")

print("Sum of Total Positive numbers :",y)


