#wap to find the largest number in a list

numbers=[90,30,40,50,60,70,80]
largest=numbers[0]

for num in numbers:
    if num > largest:
     largest = num

print("Largest Numbers :",largest)
