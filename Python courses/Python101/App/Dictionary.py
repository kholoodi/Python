#child_one = ('Ahmed','Riyadh', '1-1-2021')
# Dictioary decleation key : value
#المفتاح Key في Dictionary يجب أن يكون فريد ولا يمكن أن يُكرر.
child_one = {'name':'Ahmed','brith_city':'Riyadh', 'brithday':'1-1-2021'}
print(child_one)
print(type(child_one)) #<class 'dict'>
#Access to items in dictionary
print(child_one['name'])

#print all values in dictionary
print(child_one.values()) ##dict_values(['Ahmed', 'Riyadh', '1-1-2021'])

#print all keys
print(child_one.keys()) #dict_keys(['name', 'brith_city', 'brithday'])
