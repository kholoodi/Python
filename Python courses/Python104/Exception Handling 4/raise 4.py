
# raise keyword using for stopped the program if the if condition is false

age = int(input("please, Enter your age: "))

if age < 18:
    raise Exception ('Sorry, this Game for more than 18 age ')
#the program will stopped here

print('Start game')