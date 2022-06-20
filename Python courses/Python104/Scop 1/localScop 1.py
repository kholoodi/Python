#Local Scope
def func():
    #A variable name has a local scope in func()
    name ='Nora'
    print(name)

func()
name = 'Sara'
print(name)