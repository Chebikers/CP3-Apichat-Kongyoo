class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirdition(self):
        print("Turn on : Air")

class Picup(Vehicle):
    pass
class Car(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass
car1 =  Car()
car1.turnOnAirdition()
picup1 =  Picup()
picup1.turnOnAirdition()
van1 =  Van()
van1.turnOnAirdition()
estatecare1 =  Estatecar()
estatecare1.turnOnAirdition()
