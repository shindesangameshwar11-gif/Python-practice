#wap to create a dict containing a student name,course,age,and marks, perform all operations
#acess the student name using the key
#print all keys using the keys
#print the all values
#print the all key values pairs
#update the student marks 
#add a new key grade

a={
          "name1" : "Sangam,",
          "mark1" : 99,
          "course": "BCA",
          "age" : 20,
       
          "name2" : "vicky",
          "mark2" : 35,
          "course": "BCA",
          "age" : 24,
        
           "name3" : "abhijeet",
           "mark3" : 35, 
           "course": "BCA",
           "age":19,
        
          "name4" : "jyote",
          "mark4" : 35,
          "course": "BCA",
          "age" :20,
        
           "name5" : "kunal",
           "mark5" : 35,
          "course": "BCA",
          "age":20,
           
}

print(a["name1"])
print(a.keys())
print(a.values())
print(a.items())

a.update(
    {
        "mark1":90,
        "mark2":80,
        "mark3":85,
        "mark4":70,
        "mark5":60,


    }
)

print(a)
