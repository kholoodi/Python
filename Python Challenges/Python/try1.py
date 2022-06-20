def wz(num):
    i = 2
    while i < num:
        if num % i == 0:
            print(i)
        i = i + 1

number = 20
if number < 0:
    print("nathing")
else:
    wz(number)