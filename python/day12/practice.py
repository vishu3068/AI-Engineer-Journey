class car:
    def move(self):
        print("car is moving")
class boat:
    def move(self):
        print('car is moving')
class plain:
    def move(self):
        print('plain is moving')

vehicles =[car(),boat(),plain()]
for vehicle in vehicles:
    vehicle.move()
