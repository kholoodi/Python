# With tuples can't change elements value
child_one = ('Ahmed','Riyadh', '1-1-2021')
print(child_one) # ('Ahmed', 'Riyadh', '1-1-2021')
print(type(child_one)) #<class 'tuple'>
print(child_one[0]) #Ahmed

#Onther defination for tuples
child_one = 'Ahmed','Riyadh', '1-1-2021'
print(type(child_one)) #<class 'tuple'>
print(child_one) #('Ahmed', 'Riyadh', '1-1-2021')

# list defination in python list can contain  many data type in same time
list_one = [[1, 2, 3], "Red", True, 123]

# defination tuple With tuples can't change elements value
Tuple_one = ([1, 2, 3], "Red", True)
#Onther defination for tuples
Tuple_Two = [1, 2, 3], "Red", True
print(Tuple_one)
print(Tuple_Two)
print(list_one)
