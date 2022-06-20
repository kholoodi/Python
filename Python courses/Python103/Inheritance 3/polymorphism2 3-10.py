# polymorphism same function ide in  different classes
class Circle:
    def draw(self):
        print('The code for drowing circle')

class Sequare:
    def draw(self):
        print('The code for drowing sequare')
class Triangle:
    def draw(self):
        print('The code for drowing triangle')

circle1 = Circle()
sequare1 = Sequare()
triangle1 = Triangle()

shapes = [circle1,sequare1 ,triangle1]
#The  code  with using polymorphism
for sh in shapes:
    sh.draw()
#The  code  without using polymorphism (without draw function )
#for sh in shapes:
#    if isinstance(sh, Circle):
#        print('The code for drowing circle')
#   elif isinstance(sh, Sequare):
#        print('The code for drowing sequare')
#    else:
#        print('The code for drowing triangle')
