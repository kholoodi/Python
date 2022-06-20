list_one = [9, 5, 1, 8]
list_two = ['Khadijah','Asmaa','Zainab']

list_one.sort()
list_two.sort()
print(list_one) # [1, 5, 8, 9]
print(list_two )# ['Asmaa', 'Khadijah', 'Zainab']

list_one.sort(reverse=True)
list_two.sort(reverse=True)
print(list_one) #[9, 8, 5, 1]
print(list_two) # ['Zainab', 'Khadijah', 'Asmaa']