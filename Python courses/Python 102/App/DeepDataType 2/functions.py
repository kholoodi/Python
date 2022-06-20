
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list = [1, 2, 3, 4, 5, 6]
touple = (1, 2, 3, 4, 5, 6)

#slice function
print(alphabet[slice(0,5)]) #abcde
print(alphabet[slice(0,5,2)]) #ace
print(list[slice(0,5,2)]) #[1, 3, 5]
print(touple[slice(0,5,2)]) #(1, 3, 5)

#index function
str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, send do'
print(str.index('do')) #12
the_list =[1, 2, 2, 3]
print(the_list.index(2)) #1
print(touple.index(5)) #4

#Length
print(len(str))
print(len(list))
print(len(touple))

#count
str2 = 'This is student Noora'
list1 =[1, 2, 2, 3, 3, 3, 3]
touple2 = (4, 4, 4, 4, 5, 5, 5, 5, 5, 5)
print(str2.count('s')) #3
print(str2.count('Noora')) #1
print(list1.count(2)) #2
print(touple2.count(5)) #6




