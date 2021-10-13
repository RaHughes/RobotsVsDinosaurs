from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(Robot('Optimus-prime'))
        self.robots.append(Robot('Bumble-bee'))
        self.robots.append(Robot('Megatron'))