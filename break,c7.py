#wap to take a 10 numbers from the user, stop the loop immediately when user type negative numbers

while True:

    a=int(input("Enter 10 numbers :"))

    if a < 0:
        break

    print("You entered :",a)

print("Loop Ended")

