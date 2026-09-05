#electricity bill calculator
a=int(input("Enter Electricity Units:"))

if(a<=100):
    print('Bill:',a*5)
elif(a<=200):
    print('Bill:',a*7)
elif(a<=300):
    print('Bill:',a*10)
else:
    print('Bill:',a*12)
