from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Sword', 40)

    def attack(self, dinosaur):
        print()
        print(f'{self.name} attacks {dinosaur.name} with a {self.weapon.name} for {self.weapon.attack_power}!')
        dinosaur.health -= self.weapon.attack_power
        print()
        print(f'{dinosaur.name} only has {dinosaur.health} health left!')