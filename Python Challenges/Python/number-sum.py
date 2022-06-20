def number_sum(num):
    if num == 1:
        return 1
    elif num ==0:
        return 0
    else:
        return num + number_sum(num -1)


print( number_sum(3))
print( number_sum(2))
print( number_sum(5))
print( number_sum(7))