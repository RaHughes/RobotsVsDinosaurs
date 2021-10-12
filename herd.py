from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('T-Rex', 100))
        self.dinosaurs.append(Dinosaur('Stego', 100))
        self.dinosaurs.append(Dinosaur('Raptor', 100))     