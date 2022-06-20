#map تسستقل دالة وقائمة وتطبق الدالة على عناصر القائمة
numbers =[5, 10, 20, 25, 50]
#sq_number = []
#def square(numbers):
#    for num in numbers:
#        sq_number.append(num ** 2)
#    return sq_number

#print(square(numbers)) #[25, 100, 400, 625, 2500]
#-------------------------
def square(num):
    return num **2
print(list(map(square, numbers)))
#[25, 100, 400, 625, 2500]