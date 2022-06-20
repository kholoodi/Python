def max_element(arr):
    Max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > Max:
            Max = arr[i]
    return Max

def main():
    array = [2 , 4 , 9 , 23 , 435]
    print(max_element(array))

    array = [-32 , -44 , -9 , 3 , -8]
    print(max_element(array))

    array = [-99 , -314 , 0 , -200 , -23]
    print(max_element(array))

    array = [72 , 86 , 23 , 70 , 1]
    print(max_element(array))
    
    array = [55 , 64 , 0 , 11 , 4]
    print(max_element(array))
   

if __name__ == '__main__': 
    main()