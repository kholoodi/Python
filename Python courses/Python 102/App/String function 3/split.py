#Using split() for convert string to list
text = 'A, B, C'
print(text.split()) #['A,', 'B,', 'C']
print(text.split(',')) # ['A', ' B', ' C'] split depend on ','

text = 'This is a srting'
print(text.split('s')) # ['Thi', ' i', ' a ', 'rting'] remove 's' when split
print(text.split('S')) # ['This is a srting'] case sentsive
print(text.split('s', 1)) #['Thi', ' is a srting'] split one time 