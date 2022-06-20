# Argument Unpacking is separated element in list or tuple or string  and used them as position argument
def info(name1, name2, name3):
    print("First student's name: ", name1)
    print("Second student's name: ", name2)
    print("Third student's name: ", name3)

names = 'Abdullah', 'Sara', 'Ahmed'
info(*names) # => info(names[0], names[1], names[2])