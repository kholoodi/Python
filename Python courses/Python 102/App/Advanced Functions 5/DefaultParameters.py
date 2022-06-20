#Default Parameters or optional parameters
#using default values to parameters when we don't passed argument
def info( name = 'Ghadah', age = 16, course ='Python'):
    print('My name is '+name + ', I am', age,'years old and I am taking ' + course+ 'course.')
#In default argument order is important
info()
info('Noor')
info('Noor', 25)
info('Noor',19, "JavaScript")