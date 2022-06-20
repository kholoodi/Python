# Access Modifiers With Methods

class Employees:
    def __init__(self, name):
        self.name = name
        self._tel = '+96655xxxxx'
        self.__salary = 1700
    #Prodectd  Method
    def _job_title(self):
        print('Programmer')

    def __give_reise(self):
        self.__salary = self.__salary + 500
        print('Your salary now is:', self.__salary)
    def get_reise(self):
        self.__give_reise()

emp1 = Employees('Saud')
emp1._job_title()
#emp1.__give_reise() #Error  No direct Asccess
emp1.get_reise()