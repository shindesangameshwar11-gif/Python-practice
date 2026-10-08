#Write a Python program to perform indexing, slicing, negative slicing, count(), and index() operations on a tuple.

x=(1,2,1,3,1,5,2,3,7,8,1,3,4,5,9,7,6,0)
print(x[0]) 
#indexing operation                   

print(x[0:5])
#slicing operation

print(x[-5::])
#negative slicing

print(x.count(1))
#count elements

print(x[8])
#index element