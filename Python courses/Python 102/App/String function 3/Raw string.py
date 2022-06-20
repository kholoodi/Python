# using "R" or "r" before string for print back slash  '\' or '\n' or '\t'
str = '\t python'
#file_path = 'D:\xTuwaq\Python\xPython 102\xApp\String function 3\xalphaCase.py'

print(str)
#print(file_path) # error
#for resove we an type:
file_path1 = 'D:\\xTuwaq\\Python\\xPython 102\\xApp\\String function 3\\xalphaCase.py'
print(file_path1)

#OR usinr Raw string "R" or "r"
str = r'\t python'
file_path = R'D:\xTuwaq\Python\xPython 102\xApp\String function 3\xalphaCase.py'
print(str) #\t python
print(file_path) #D:\xTuwaq\Python\xPython 102\xApp\String function 3\xalphaCase.py
#Note: we can't use "r" with single back slash like :
#print(r'\') => error
print('\\') #\