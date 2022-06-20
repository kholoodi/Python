#try...expect  to handling the exception error
# try => the code possible  error (test code)
# except => the code works when an error happens in try code
#else => the code works when error happens in try code
#finally => the code works when if the error happens in try code or not
try:
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    print("the result: ", num1/num2)
except:
    print('Error..!!')
else:
    print('No error')
finally:
    print('End the program')