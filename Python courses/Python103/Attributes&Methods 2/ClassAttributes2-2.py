#Class Attribute = static member = static data
#Class attribute is the attribute has one value for all object
class Student:
    #Add class attribute static member
    university_name ='King Saud University'
    def __init__(self, name , age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades


student1 = Student('Nouf', 21, 'xx00', [95,85,92])
student2 = Student('Hessan', 19, 'xx01', 95)

print(student1.university_name)
print(student2.university_name)