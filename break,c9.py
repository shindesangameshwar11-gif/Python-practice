#wap to repeatedly ask the user to entered number and skip negative numbers and print only positive numbers and stop the program when user entered 0

while True:

    a=int(input("Enter Number :"))

    if a==0 :
        break

    elif a>0:
        print("You entered :",a)

    else:
        continue

print("End of loop")

