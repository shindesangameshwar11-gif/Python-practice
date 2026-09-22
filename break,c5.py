#wap to take numbers from the user . and stop taking input when the user entered 0

while True:
    num = int(input("Enter a number :"))

    if num == 0:
        break

    print("You entered :",num)

print("loop ended")