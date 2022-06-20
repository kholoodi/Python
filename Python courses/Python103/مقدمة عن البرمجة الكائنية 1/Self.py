# self is an object which called at particular point
#self is the first parameter in class methods it can hold any name X for example
class Student:
    def talk(self):
        print(self)

stu1 = Student
stu2 = Student
stu1.talk() # self refer to stu1

stu2.talk() # self refer to stu2