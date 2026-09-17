#wap to access a key that does not exits a dicitonary using the get() method "key not found" if the key does not exits
info={

     "name" : "Sangam",
     "age" : 20,
     "location" : "udgir",
     
}

a=info.get("country")

if a is None:
    print("key not found")
else:
    print(a)