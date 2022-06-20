class Student:
    def print_info(self):
        print('This is a code for class Student ')

class Teacher:
    def print_info(self):
        print('This is a code for class Teacher ')


stduent1 = Student()
teacher1 = Teacher()
#Duck Typing the polymorphism with Python
#Duck typing  القدرة على استدعاء الدالة للكائن بدون التحقق من نوعه
#قراءة خصائص الكائن اولاً بدلاً من البدء بالتحقق من نوعة (والذي يكلف مزيداً من الوقت )

def func(obj):
    obj.print_info()

func(stduent1)
func(teacher1)

