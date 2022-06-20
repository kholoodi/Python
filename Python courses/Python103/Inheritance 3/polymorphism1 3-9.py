# Polymorphsim same function ide in  different classes
class Student:
    def print_info(self):
        print('This is a code for class Student ')

class Teacher:
    def print_info(self):
        print('This is a code for class Teacher ')


stduent1 = Student()
teacher1 = Teacher()

stduent1.print_info()
teacher1.print_info()