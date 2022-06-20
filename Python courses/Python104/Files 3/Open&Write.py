#open function for open the file or create a new one if not existing
# 'w' write mode for able to write on the file
file = open('text.txt', 'w')
file.write('Hello, world')
#close the file
file.close()