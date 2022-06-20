# receiving parameters  as positional argument

def my_func(*items):
    print(items)



items = ['a','b','c']
my_func(items) #(['a', 'b', 'c'],)
my_func(*items) # ('a', 'b', 'c')