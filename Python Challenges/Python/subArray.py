def sub_arrays(arr1, arr2):
    arr3 =[]
    for i in range(0, len(arr2)):
        arr3[i] = arr2[i] - arr1[i]
    return arr3


print(sub_arrays([4 , 2 , 88], [2 , 4 , 88]))
print(sub_arrays([93 , 22 , 7], [-3 , 4 , 0]))
    