def sort_array(array):

  for i in range(0,len(array)):
    
    if array[i] > array[i+1]:
      temp = array[i]
      array[i] = array[i+1]
      array[i+1] = temp

      
  
  return array

def main():
  arr = [2 , 4 , 9 , 23 , 435]
  print(sort_array(arr))
  arr = [32 , 44 , 9 , 3 , 8]
  print(sort_array(arr))
  arr = [99 , 314 , 8 , 200 , 23]
  print(sort_array(arr))
  arr = [72 , 86 , 23 , 70 , 1]
  print(sort_array(arr))
  arr = [55 , 64 , 1 , 11 , 4]
  print(sort_array(arr))
  arr = [7]
  print(sort_array(arr))



if __name__ == '__main__': 
    main()