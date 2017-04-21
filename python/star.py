import random


class little_star:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(-self.width, self.width)
        self.y = random.randint(-self.height, self.height)
        self.z = random.randint(0, self.width)
        self.pz = self.z

    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.x = random.randint(-self.width, self.width)
            self.y = random.randint(-self.height, self.height)
            self.z = self.width
            self.pz = self.z
