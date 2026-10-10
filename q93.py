#Write a Python program to create a student dictionary and perform accessing values
# get(), keys(), values(), items(), and update() operations.

x = {
      "name" : "Sangam",
      "course" : "bca",
      "cgpa" : 8,
      "skill" : "python"
    }

print(x.get("cgpa"))
#get operaton

print(x.keys()) 
#keys operation

print(x.values()) 
#values operation
   
print(x.items())
#items operation

x.update({"mark" : 80})
print(x)
#update operation
