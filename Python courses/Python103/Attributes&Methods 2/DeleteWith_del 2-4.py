#Delete an  Attribute
#Delete an object
class Student:
    def __init__(self, name , age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print("My name is :", self.name)


student1 = Student('Nouf', 21, 'xx00', [95,85,92])
student2 = Student('Hessan', 19, 'xx01', 95)
#Add attribute to object
student2.v_hours = 16
print(dir(student2))

#Delete the attribute
del student2.v_hours
print(dir(student2)) # we see the v_hours is deleted  from  student2 object

#delete an object
del student1
print(student1) #error student1 is not defined
print(student2)
