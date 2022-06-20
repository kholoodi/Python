#Read function for reading from the file
# first must open with read mod
file = open('text.txt', 'r')
#print(file.read()) # read all the file
print(file.read(5)) # read first 5 letters
file.close()