#import math
def raduis(circumference):
	#return circumference / (2 * math.pi)
    return circumference / (2 * 3.14)


def main():
    print(raduis(4))
    print(raduis(6.4))
    print(raduis(0))
    print(raduis(4.7))


if __name__ == '__main__': 
    main()