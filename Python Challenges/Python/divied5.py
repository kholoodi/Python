def divisible_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

def main():
    print(divisible_by_five(5))
    print(divisible_by_five(43))
    print(divisible_by_five(73))
    print(divisible_by_five(50))
    print(divisible_by_five(56))

   

if __name__ == '__main__': 
    main()