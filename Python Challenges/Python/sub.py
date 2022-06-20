
def sub(a,b):
    if a < 0 and b < 0:
        return - (a-b)
    return a -b 
    
def main():
    print(sub(10,5))
    print(sub(3,-3))
    print(sub(-4,1))
    print(sub(0,-1))
    print(sub(0,0))
    print(sub(-4,-96))
    

if __name__ == '__main__': main()