# constructor هي دالة تقوم باسناد القيم للخصاص الكلاس
#Construcor knows as init() ==> short of  initialization
class Student:
    def __init__(self, name , age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print("My name is :", self.name)


student1 = Student('Nouf', 21, '00xx', 95) # error if we don't have constructor init() method


