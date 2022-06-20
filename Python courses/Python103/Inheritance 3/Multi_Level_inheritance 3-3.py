#Multi Level Inheritance
# GrandParent <= Parent <= Child
class GrandParent:
    def g_display(self):
        print('This is Grandparent class')

class Parent(GrandParent):
    def p_display(self):
        print('This is Parent class')

class Child(Parent):
    def C_display(self):
        print('This is Child class')

#Child class has access to all parent classes
child1 = Child()
child1.C_display()
child1.p_display()
child1.g_display()