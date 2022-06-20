class Vehicle:
    def __init__(self, company, owner, color, speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.speed = speed

    def move(self):
        print('The vehical has move')

    def stop(self):
        print('The vehicle has stop')

# Car class inheritance from Vehical
class Car(Vehicle):
    def dispaly(self):
        print('This is the Car class')

class Track(Vehicle):
    def dispaly(self):
        print('This is the Track class')

car1 = Car('Jeeb', 'Nada', 'Black', 0)
print(car1.company)
car1.move()

track1 = Track('Mercedes', 'Mohemmed', 'white', 0)
print(track1.company)
track1.move()