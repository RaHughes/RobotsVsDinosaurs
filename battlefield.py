from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.turn = 0

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs! Get ready for one epic battle!')
        print()
        print(f'In the Robot Fleet we have {self.fleet.robots[0].name}, {self.fleet.robots[1].name}, and {self.fleet.robots[2].name}!') 
        print()
        print(f'In the Dinosaur Herd we have {self.herd.dinosaurs[0].name}, {self.herd.dinosaurs[1].name}, and {self.herd.dinosaurs[2].name}!')
        print()
    
    def battle(self):
        while self.fleet.robots != [] or self.herd.dinosaurs != []:
            self.check_health()
            random_robot = random.choice(self.fleet.robots)
            self.robot_turn(random_robot)
            self.check_health()
            random_dino = random.choice(self.herd.dinosaurs)
            self.dino_turn(random_dino)    


    def dino_turn(self, dinosaur):
        print(f'Looks like its {dinosaur.name} turn!')
        print()
        self.show_dino_opponent_options(dinosaur)

    def robot_turn(self, robot):
        print(f'Looks like its {robot.name} turn!')
        print()
        self.show_robo_opponent_options(robot)

    def show_robo_opponent_options(self, robot):
        names = []
        for dino in self.herd.dinosaurs:
            names.append(dino.name)
        target = input(f'Which Dinosaur would you like to attack? {names}: ')
        for dino in self.herd.dinosaurs:
            if target == dino.name:
                robot.attack(dino)
                print()  

    def show_dino_opponent_options(self, dino):
        names = []
        for robot in self.fleet.robots:
            names.append(robot.name)
        target = input(f'Which Robot would you like to attack? {names}: ')
        for robot in self.fleet.robots:
            if target == robot.name:
                dino.attack(robot)
                print()

    def display_winners(self):
        if self.fleet.robots == []:
            print('Looks like the Dinosaurs have won!')
        elif self.herd.dinosaurs == []:
            print('Looks like the Robots have won!')    

    def check_health(self):
        for dino in self.herd.dinosaurs:
            if dino.health <= 0:
                print(f'Looks like {dino.name} was defeated!')
                self.herd.dinosaurs.remove(dino)
            else:
                continue    
        for robot in self.fleet.robots:
            if robot.health <= 0:
                print(f'Looks like {robot.name} was defeated!')
                self.fleet.robots.remove(robot)   
            else:
                continue         
