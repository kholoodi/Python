#Argument dictionary Packing  is receiving parameters  as as dictionary form
#parameters are keyword Argument
def info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print('My name is', kwargs['name'])


info(name= 'Ali', age = 33)
#{'name': 'Ali', 'age': 33}
#<class 'dict'>