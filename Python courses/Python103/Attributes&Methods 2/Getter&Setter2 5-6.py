#Get & Set

class MyInteger:
    def set_val(self, val):
        if type(val) == int:
            self.val = val
        else:
            print('This value is not an integer')

    def get_val(self):
        return self.val

    def incerment_val(self):
        self.val+= 1


i = MyInteger()

i.set_val(9)
print(i.get_val())

i.set_val('Hello')
print(i.get_val())

#Error
#i.val = 'Hello'
#i.incerment_val()
#print(i.get_val())