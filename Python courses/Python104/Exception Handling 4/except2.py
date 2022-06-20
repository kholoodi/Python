# determine the Error type

mylist = [1,2,0]

try:
    print('the result: ', mylist[4] / mylist[2])

#except for the first error happened works
except ZeroDivisionError:
    print('ZeroDivisionError..!!')

except IndexError:
    print('IndexError')
