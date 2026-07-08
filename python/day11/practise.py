class vehicle:
    def start(self):
        print('vehicle started')
class car(vehicle):
    def drive(self):
        print('car is driver')

car1=car()
car1.start()
car1.drive()