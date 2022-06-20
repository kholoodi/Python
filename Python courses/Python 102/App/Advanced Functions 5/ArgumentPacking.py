# Argument Packing is receives unlimited  parameters in the sametime and saved  them in a tuple
def avg(*args):
    print(args)
    print(type(args))
    total = sum(args)
    leng = len(args)

    average = total / leng
    print(average)
avg(2, 6) # 4.0