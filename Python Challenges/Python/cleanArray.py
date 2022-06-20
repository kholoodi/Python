def clean_array(arr):
    array = []
    for i in arr:
        if i != None:
            array.append(i)
    return array

print(clean_array([2,None,4,5]))
print(clean_array([None,7,8,None,9]))
print(clean_array([None,None,None,None]))
print(clean_array([2,7,8]))