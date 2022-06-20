#Unpackin dictionary is convert dictionary to keyword argument
def info(name, age):
    print('My name is ', name, 'and I am ',age, 'years old')

d = {'name': 'Ali', 'age': 22}
info(**d) # => info(name='Ali', age= 22)
