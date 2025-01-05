import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx: int, dy: int, dz: int):
        if self._cords[2] < 0:
            print(f"It's too deep, I can't dive :(")
        else:
            self._cords = [self._cords[0] + dx * self.speed, self._cords[1] + dy * self.speed, self._cords[2] + dz * self.speed]
    
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")
    
    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, speed, _cords=[0, 0, 0]):
        super().__init__(speed, _cords)

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed, _cords=[0, 0, 0]):
        super().__init__(speed, _cords)
    
    def dive_in(self, dz: int):
        self._cords[2] -= (abs(dz) * (self.speed / 2))
    

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed, _cords=[0, 0, 0]):
        super().__init__(speed, _cords)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed, _cords=[0, 0, 0]):
        super().__init__(speed, _cords)
        self.sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()