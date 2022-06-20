def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes_nums(array):
    arr =[]
    for i in array:
        if isprime(i):
            arr.append(i)
    return arr



print(primes_nums([5, 38, 33, 60, 56, 7]))
print(primes_nums([53,20,71]))
print(primes_nums([31,44]))
print(primes_nums([12,4, 44,89]))