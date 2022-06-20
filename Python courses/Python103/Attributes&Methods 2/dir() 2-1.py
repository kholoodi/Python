# dir() function return list of all the object attributes

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

print(dir(student1))
print(dir(student2))


