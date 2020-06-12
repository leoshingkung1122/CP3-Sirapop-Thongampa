class Vehicle():
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on air !!!")
        print("")

class Car(Vehicle):
    def carIdentity(self):
        print("This is a Car.")

class Van(Vehicle):
    def vanIdentity(self):
        print("This is a Van.")

class PickUp(Vehicle):
    def pickUpIdentity(self):
        print("This is a Pickup.")

class EstateCar(Vehicle):
    def estateCarIdentity(self):
        print("This is an Estate car")

car1 = Car()
car1.carIdentity()
car1.turnOnAirConditioner()

van1 = Van()
van1.vanIdentity()
van1.turnOnAirConditioner()

pickUp1 = PickUp()
pickUp1.pickUpIdentity()
pickUp1.turnOnAirConditioner()

estateCar1 = EstateCar()
estateCar1.estateCarIdentity()
estateCar1.turnOnAirConditioner()


