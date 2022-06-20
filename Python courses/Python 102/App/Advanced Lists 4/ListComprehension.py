#List Comprehension is concept of create a new list which depend on existed one under specific condition
lst = [1, 2, 3, 4, 5]
#multiplied_list = []
#for num in lst:
#    if(num >3) and num %5 == 0 :
#        multiplied_list.append(num*2)
#print(multiplied_list) #[2, 4, 6, 8]
#-----------------------
multiplied_list = [num*2 for num in lst ]
print(multiplied_list) #[2, 4, 6, 8]
#with condation
multiplied_list = [num*2 for num in lst if num >3]
print(multiplied_list) #[8,10]

#with two condations
multiplied_list = [num*2 for num in lst if num >3 and num %5 ==0]
print(multiplied_list) #[10]