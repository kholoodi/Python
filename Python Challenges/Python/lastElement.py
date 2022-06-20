def last_elm(arr):
    return arr[len(arr)-1]
  

def main():
    print(last_elm([2 , 4 , 9 , 23 , 435]))
    print(last_elm([32 , 44 , 9 , 3 , 8]))
    print(last_elm([99 , 314 , 8 , 200 , 23]))
    print(last_elm([72 , 86 , 23 , 70 , 1]))
    print(last_elm([55 , 64 , 0 , 11 , 4]))

if __name__ == '__main__': 
    main()