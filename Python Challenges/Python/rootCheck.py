import math
def root_check(sqare, num):
    number = int(math.sqrt(sqare))
    if number == num:
        return num
    else:
        return 0


print(root_check(8, 2))
print(root_check(81, 9))
print(root_check(36, 6))
print(root_check(16, 2))