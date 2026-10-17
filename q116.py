# Write a Python program to print numbers from 1 to 10 and skip the number 5 using continue.

w=1
while w<=10:
    if w==5:
        w+=1
        continue
    print(w)
    w+=1
    
      