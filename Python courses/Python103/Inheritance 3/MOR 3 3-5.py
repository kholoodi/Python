# Depth -First is an algorithm with python use it for order resolution
#تحليل الطلبorder resolution
class A:
    def do_this(self):
        print('Doing This in calss A')

class B(A):
    pass

#If A is Parent of C too
class C(A):
    def do_this(self):
        print('Doing This in calss C')

class D(B, C):
    pass

obj = D()
obj.do_this() #Doing This in calss C