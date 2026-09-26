#wap to count the number using of vowels in a given string using a for loop

x=(input("Enter Words :"))
y=0

for char in x:
    if char in "aeiouAEIoU":
        y = y + 1

print("Numbers of vowels :",y)