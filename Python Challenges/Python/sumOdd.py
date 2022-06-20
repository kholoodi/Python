def sumOdd(arr):
    sum = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 != 0:
            sum = sum + arr[i]
    return sum


print(sumOdd([1,2,3,4,5]))
print(sumOdd([2,9,4,7]))
print(sumOdd([34,2,5,8]))
print(sumOdd([2,4,8]))
