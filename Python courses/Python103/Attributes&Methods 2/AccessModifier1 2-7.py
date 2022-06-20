# Access Modifiers With attributes 

class Employees:
    def __init__(self, name):
        #public attribute
        self.name = name
        #Protected attribute
        self._tel = '+96655xxxxx'
        #pravite attribute
        self.__salary = 1700
    def get_salary(self):
        return self.__salary

emp1 = Employees('Saud')

print(emp1.name) # Saud
print(emp1._tel) # 96655xxxxx
#print(emp1.__salary) # Error can't access if don't use get()
#if we use get
print(emp1.get_salary())

#if we set value to pravite attribute
#emp1.__salary = 5000
#print(emp1.__salary)
