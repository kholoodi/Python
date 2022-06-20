# Multiple Inheritance
# A class inherited from many classes
class Polygon:
    def p_display(self):
        print('This is Polygon class')

class Shape:
    def sh_display(self):
        print('This is Shape class')

#Seqare has access for all parents   
class Sequare(Polygon, Shape):
    def s_display(self):
        print('This is Sequare class')

sq = Sequare()
sq.s_display()
sq.p_display()
sq.sh_display()
