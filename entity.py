import math

class Entity():
    def __init__(self, image, pos, speed, specie, dir_angle):
        self.image = image
        self.pos = pos
        self.speed = speed
        self.dir_angle = dir_angle
        self.specie = specie #0 = Rock, 1 = Paper, 2 = Scissors

    def move(self, dir_angle):
        self.dir_angle = dir_angle
        self.pos[0] += self.speed * math.cos(self.dir_angle)
        self.pos[1] += self.speed * math.sin(self.dir_angle)

    def collide(self, ennemy):
        if (ennemy.pos[0] <= self.pos[0] <= ennemy.pos[0] + 20 or ennemy.pos[0] <= self.pos[0] + 20 <= ennemy.pos[0] + 20) and (ennemy.pos[1] <= self.pos[1] <= ennemy.pos[1] + 20 or ennemy.pos[1] <= self.pos[1] + 20 <= ennemy.pos[1] + 20):
            return True
