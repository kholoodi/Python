def cumulative_addition(array):
  sum = 0 
  length = len(array)
  for i in array:
      sum += i
  return [sum, length]

def main():
    print(cumulative_addition([2 , 4 , 9 , 23 , 435]))
    print(cumulative_addition([32 , 9 , 3 , 8]))
    print(cumulative_addition([99 , 314 , 8 , 200 , 23 , 2]))
    print(cumulative_addition([72 , 86]))
    print(cumulative_addition([55]))

if __name__ == '__main__': 
    main()
