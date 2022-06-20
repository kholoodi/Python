def foo(*args):
    print(args)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
foo(*l1, *l2)
#(1, 2, 3, 4, 5, 6)