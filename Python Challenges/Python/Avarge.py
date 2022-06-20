def average(arr):
    sum =0
    for i in arr:
        sum += i
    return sum /len(arr)

def main():

  arr1 = [2,4,9,23,435]
  print(average(arr1))
  arr2 = [0,44,9,3,8]
  print(average(arr2))
  arr3 = [99,23]
  print(average(arr3))
  arr4 = [72,86,23,70,1]
  print(average(arr4))
  arr5 =[55,2,96]
  print (average(arr5))

if __name__ == '__main__': main()

