def get_mean(arr):
    sum =0
    for i in arr:
        sum = sum +i
    return float(sum / len(arr))

def main():
    a = get_mean([1,2,3,4,5])
    print(a)
    a = get_mean([8,9])
    print(a)
    a = get_mean([1,5,7,3])
    print(a)
    a = get_mean([2,7,1,9,8])
    print(a)
 
if __name__ == '__main__': main()