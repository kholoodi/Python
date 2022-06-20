
text = 'A, B, C'
string_to_list =text.split(',')
print(string_to_list)
#Join convert list to string
list_to_string = ' '.join(string_to_list)
print(string_to_list) #['A', ' B', ' C']
print(list_to_string) #A  B  C

list_to_string = '%'.join(string_to_list)
print(list_to_string) #A% B% C

#join also convert the dictionary and tuple to sting
