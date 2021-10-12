class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        print()
        print(f'{self.name} attacks {robot.name} with a powerful bite for {self.attack_power}!')
        robot.health -= self.attack_power    
        print()
        print(f'{robot.name} only has {robot.health} health left!')
