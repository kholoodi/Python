def smallest_number(arr):
    Min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < Min:
            Min = arr[i]
    return Min

def main():
    array = [13 , 2 , 1 , 4 , 106]
    print(smallest_number(array))

    array = [90 , 7 , 56 , 33 , 83]
    print(smallest_number(array))

    array = [91 , 67 , 223 , 943 , 34]
    print(smallest_number(array))

    array = [43 , 3 , -6 , 55 , 205]
    print(smallest_number(array))
    
    array = [5 , 0 , 1 , 21 , 43]
    print(smallest_number(array))
   

if __name__ == '__main__': 
    main()