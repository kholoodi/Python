#الدالة filter تسقبل دالة وlist  تطبق الدالة على عناصر list
ages = [30, 9, 15, 22, 17, 44, 26, 5]
#adult = []
#def filter(arr):
#    for i in arr:
#        if i >= 18:
#            adult.append(i)
#    return adult
#-----------------
def filter_ages(age):
    return age >= 18


print(list(filter(filter_ages, ages))) #[30, 22, 44, 26]

#list founction converts the reslut to list