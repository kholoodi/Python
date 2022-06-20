#Slicing concept
#close Range
text = 'This is Python Course'
print(text[8:14]) #Python

#open Range
#[from:] EX: for print 'Python Course'
print(text[8:]) #from index 8 to end
print(text[-13:]) # with miunce index

#[:to] EX: for print 'This is'
print(text[:7]) #from start to index 7

#[:] all string
print(text[:])#This is Python Course

#slicing work with list and touple too
list = [1, 2, 3, 4, 5, 6]
touple = (1, 2, 3, 4, 5, 6)
print(list[-3:]) #[4, 5, 6]
print(touple[-3:]) #(4, 5, 6)

#slicing jump [start: end: setp]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0:7:2]) #aceg
print(alphabet[5:0:-1]) #fedcb
print(list[3:0:-2]) #[4, 2]
print(touple[3:0:-2]) #(4, 2)



