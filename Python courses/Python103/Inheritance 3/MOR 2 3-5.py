# Depth -First is an algorithm with python use it for order resolution
#تحليل الطلبorder resolution   
class A:
    pass

class B(A):
    pass

class C:
    def do_this(self):
        print('Doing This in calss C')

class D(B, C):
    pass

#If Do-this() is only in class C 
obj = D()
obj.do_this() #Doing This in calss C