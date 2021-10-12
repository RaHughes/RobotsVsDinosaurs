from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino_one = Dinosaur('T-Rex', 40)
        dino_two = Dinosaur('Stego', 20)
        dino_three = Dinosaur('Raptor', 10) 
        self.dinosaurs.append(dino_one, dino_two, dino_three)
        for dino in self.dinosaurs:
            print(dino.name)       