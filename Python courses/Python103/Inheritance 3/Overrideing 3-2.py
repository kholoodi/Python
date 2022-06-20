
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(speed):...


    def make_sound(self):
        print('Sound..')

class Cat(Animal):
    def make_sound(self):
        print('Mewo..')

cat1 = Cat('lili', 'Brown')
cat1.make_sound()

