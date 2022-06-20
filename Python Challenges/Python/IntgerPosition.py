def less_or_more_than_zero(number):
    if number == 0:
        a="Equal to zero"
    elif number > 0:
        a="Greater than zero"
    elif number < 0:
        a="Less than zero"
    return a


def main():
    print(less_or_more_than_zero(9))
    print(less_or_more_than_zero(0))
    print(less_or_more_than_zero(-2))
    print(less_or_more_than_zero(-3))
    print(less_or_more_than_zero(49))

   

if __name__ == '__main__': 
    main()