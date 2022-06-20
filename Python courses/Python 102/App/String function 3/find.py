#find function for search
#looking for spcial charater in string
#return it index if found
#return -1 if not found

str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, send do'
print(str.find('do')) #12 first matching
print(str.rfind('do'))  # 62 last matching
print(str.find('DO')) # -1 Case sentsive
print(str.find('it', 50,60)) # 53 search in reange


