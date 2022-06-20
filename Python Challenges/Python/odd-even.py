def odd_even(number):
  if number % 2 == 0:
      print("زوجي")
  else:
      print("فردي")

def main():
    odd_even(9)
    odd_even(1)
    odd_even(20)
    odd_even(3)
    odd_even(48)

if __name__ == '__main__': main()