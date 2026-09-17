#wap to create a dictionary containing student name,age and marks. 
#use the update method to the change the student marks and grades.
a={
      "name1" : "Sangam,",
       "mark1" : 99,
       "grade1" : "B",
    
      "name2" : "vicky",
      "mark2" : 35,
      "grade2" : "B",
    
       "name3" : "abhijeet",
       "mark3" : 35, 
       "grade3" : "C",
    
      "name4" : "jyote",
      "mark4" : 35,
      "grade4" : "B",
    
       "name5" : "kunal",
       "mark5" : 35,
       "grade5" : "B",
     
}

a.update({"mark1": 100 })
a.update({"grade1":"A"})
print(a)

a.update({"mark2": 90 })
a.update({"grade2":"A"})
print(a)

a.update({"mark3": 92 })
a.update({"grade3":"A"})
print(a)

a.update({"mark4": 95})
a.update({"grade4":"A"})
print(a)

a.update({"mark5": 98 })
a.update({"grade5":"A"})
print(a)


