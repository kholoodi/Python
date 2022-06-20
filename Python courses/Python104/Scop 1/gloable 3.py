# global  is  a keyword use for make local variable a global variable

def func():
    global name
    name ='Nora'
    print(name)

func()
print(name) # this will be wrong if don't use global  variable
X = 88

def func1():
    print(X)

func1()