# mor() function to know the priority for  order resolution
class A:
    def do_this(self):
        print('Doing This in calss A')

class B(A):
    pass

class C:
    def do_this(self):
        print('Doing This in calss C')

class D(B, C):
    pass
#Using mor()
print(D.mro())
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]