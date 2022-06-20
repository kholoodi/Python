# using keyword  argument means give the arguments values when calling function
# arguments = parameters (same numbers and same names)
# no need to keep order with keyword argument
def info (age, name):
    print('My name is ',name,'and Iam ',age,'years old')


info(name = 'Omer', age = 22)
info( age = 22, name = 'Omer')
#info(first_name = 'Omer', age = 22) #error

# if we use position and keyword argument in same calling
# position argument must be first
# and we must match the order with their parameters

#info(name = 'Omer', 22)#error
info(16, name = 'Omer')