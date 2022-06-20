
def greet():
    name = input('Please enter your name:')
    time = input('Please enter time now:')
    print("Good " + time + "," + name + "!")

greet()

def print_nmbers(n):
    for i in range(1,n):
        print(i)

print_nmbers(5)

def add(first,second):
    print(first + second)

add(4,5)
add('Good ','morning')

def sub(first, second):
    return  first - second

value = sub(7,2) - sub(3,2)
print(value)

print_nmbers(sub(9,4))
