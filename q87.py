#Write a Python program to add a "grade" key to a student dictionary using update().

a = {
       "name" : "Sangam shinde",
       "course" : "BCA",
       "cgpa" : 7.5,
       "marks" : 450, 
    }

a.update({"grade" :"B+"})
print(a)
