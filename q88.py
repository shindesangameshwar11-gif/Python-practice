#Write a Python program to update the age and city of a person using update().

x = {
      "name" : "Sangam",
      "city" : "mumbai",
      "age" : 20,
      "course" : "bca" 
    }

x.update({
            "city": "pune",
            "age" : 21
        })

print(x)
