class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def details(self):
        print('brand: ',self.brand)
        print('model: ',self.model)
        print('price: ',self.price)
car1=car('toyoto','fortuner',5000000)
car2=car('tata','sierra',3000000)
car1.details()
car2.details()