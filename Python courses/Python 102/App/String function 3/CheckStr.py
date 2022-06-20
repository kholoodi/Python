values = 'A987'
#if the string has alph and number onlty return Ture
print(values.isalnum()) #True
values = 'A9 87'
print(values.isalnum()) #False

#if stirng has number only
print(values.isdigit())#False 
values = '987'
print(values.isdigit())  #True