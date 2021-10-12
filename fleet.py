from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot('Megatron')
        robot_two = Robot('Optimus Prime')
        robot_three = Robot('Bumble Bee')
        self.robots.append(robot_one, robot_two, robot_three)
        for robot in self.robots:
            print(robot.name)