class Person:
    def __init__(self, firstname, surname, tel):
        self.firstname = firstname
        self.surname = surname
        self.tel = tel

    def full_name(self):
        return self.firstname+" " +self.surname

#Access to init() in parent class  by class name
class Employees(Person):
    def __init__(self, firstname, surname,tel, salary):
        Person.__init__(self, firstname, surname, tel)
        self.salary = salary

    def give_reise(self, amount):
        self.salary = self.salary + amount

emp1 =Employees(1700, 'Ali', 'Saud','+96655xxxxxx')



