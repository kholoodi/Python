def sum_even(arr):
    sum = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            sum = sum + arr[i]
    return sum


print(sum_even([1,6,3]))
print(sum_even([2,7,5,10,0]))
print(sum_even([33,2,5,8]))
print(sum_even([2,4,8]))