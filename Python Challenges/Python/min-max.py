def largest_smallest(array):
    Max = array[0]
    Min = array[0]

    for i in range(1,len(array)):
        if array[i] > Max:
            Max = array[i]

        if array[i] < Min:
           Min = array[i] 
    return [Max ,Min]

def main():
    array = [2 , 4 , 9 , 23 , 435]
    print(largest_smallest(array))

    array = [32 , 44 , 9 , 3 , 8]
    print(largest_smallest(array))

    array = [99 , 314 , 8 , 200 , 23]
    print(largest_smallest(array))

    array = [72 , 86 , 23 , 70 , 1]
    print(largest_smallest(array))
    
    array = [55 , 64 , 0 , 11 , 4]
    print(largest_smallest(array))
   

if __name__ == '__main__': 
    main()