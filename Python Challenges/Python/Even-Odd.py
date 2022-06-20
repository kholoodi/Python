def odd_even(number):
  
  if number %2 == 0:
      return "زوجي"
  else:
      return "فردي"



def main():
    print(odd_even(9))
    print(odd_even(1))
    print(odd_even(20))
    print(odd_even(3))
    print(odd_even(48))

   

if __name__ == '__main__': 
    main()