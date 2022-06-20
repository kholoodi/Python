def find_element(array, element):
    for i in array:
        if i == element:
            return True
        
    return False

def main():

    print (find_element([2, 4, 1 ,9, 42], 4))
    print(find_element([43, 56, 3, 20], 70))
   
   

if __name__ == '__main__': 
    main()