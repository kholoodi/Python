def find_circle_area(radius):
  r = pow(radius,2)
  return r * 3.14


def main():
    print(find_circle_area(9))
    print(find_circle_area(2))
    print(find_circle_area(4.6))
    print(find_circle_area(3.1))


if __name__ == '__main__': 
    main()