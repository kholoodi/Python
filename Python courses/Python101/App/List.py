# list in python can contain  many data type in same time
names = [ 'Dana','Mariam','Hessah','Fatimah',1, 2, 3, True]
print(names)
# list is type of dataTypes
print(type(names)) #<class 'list'>

names = [ 'Dana','Mariam','Hessah','Fatimah']
#List's itemes can change
print(names[2]) #Access to list items by index number
names[0] = 'Ghadah'
print(names)


#Add elelment to list (in last)
names.append('Raghad')
print(names)

#insert elemnt to list
names.insert(0,'Dana')
print(names)

#remove element from list
names.remove('Hessah')
print(names)

#Remove all element in list
names.clear()
print(names)