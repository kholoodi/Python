def factorial(number):
	if number == 1 or number < 0:
		return 1
	else:
		return number * factorial(number -1)

	
def main():
	print(factorial(6))
	print(factorial(8))
	print(factorial(12))
		
if __name__ == '__main__': 
    main()
	
		