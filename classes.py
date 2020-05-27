#define a class
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = "200amp"
    def descriptionCar(self):
        print(f"The make of car is {self.make}")
        print(f"The model of car is {self.model}")
        print(f"The year of car is {self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def applyingBreak(self):
        print(f"{self.model} applied brakes")
    def desBattery(self):
        print(f"The battery of car {self.make} is {self.battery}")
    def setBatterySize(self,newSize):
        self.battery = newSize
    def getBatterySize(self):
        print(f"The size of battery for {self.make} is:{self.battery}")
#how to create objects       
car1 = Car("Honda","Civic",2019)
car2 = Car("Toyota","GLi",2020)
car1.descriptionCar()
print(car1.make)
print(car2.make)
car1.make = "Suzuki" #changing attribute via object
print(car1.make)
print(car1.battery)
car1.desBattery()
car1.battery = "300amp"
car1.getBatterySize()
car2.setBatterySize("500amp")
car2.getBatterySize()
