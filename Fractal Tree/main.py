import pygame
import math
from pygame.locals import *

# ---------------------------------------------------------------------------------------------------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ---------------------------------------------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("My Awesome Fractal Tree")
SCREEN_SIZE = (400, 400)
WIDTH, HEIGHT = SCREEN_SIZE
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

# ---------------------------------------------------------------------------------------------------------------------

class Vector():

    def __init__(self, magnitude, phase):
        self.magnitude = magnitude
        self.phase = phase          # dalam degree

    def get_x(self):
        return int(self.magnitude * math.cos(math.radians(self.phase)))

    def get_y(self):
        return int(self.magnitude * math.sin(math.radians(self.phase)))

    def coord(self):
        return (self.magnitude, self.phase)

def update(coord):
    global WIDTH, HEIGHT
    x, y = coord
    return (x + WIDTH // 2, -y + HEIGHT)

# ---------------------------------------------------------------------------------------------------------------------

init_magnitude = 100
init_phase = 90
phase_change = 40
magnitude_change = 0.65
bucket = [((0, 0), Vector(init_magnitude, init_phase))]
screen.fill((51, 51, 51))
magnitude = init_magnitude
while True:
    try:
        start_pos, branch = bucket.pop()
        magnitude, phase = branch.coord()
        x, y = start_pos
        end_pos = (x + branch.get_x(), y + branch.get_y())
        pygame.draw.line(screen, WHITE, update(start_pos), update(end_pos))

        if magnitude > 4:
            bucket.append((end_pos, Vector(magnitude * magnitude_change, phase + phase_change)))
            bucket.append((end_pos, Vector(magnitude * magnitude_change, phase - phase_change)))

        else:
            start_pos, branch = bucket.pop()
            magnitude, phase = branch.coord()
            x, y = start_pos
            end_pos = (x + branch.get_x(), y + branch.get_y())
            pygame.draw.line(screen, WHITE, update(start_pos), update(end_pos))

    except IndexError:
        pass


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273 and magnitude_change != 0.95:
                magnitude_change += 0.05
            if event.key == 274 and magnitude_change != 0.05:
                magnitude_change -= 0.05
            if event.key == 275 and phase_change != 90:
                phase_change += 10
            if event.key == 276 and phase_change != 10:
                phase_change -= 10

            bucket = [((0, 0), Vector(init_magnitude, init_phase))]
            screen.fill((51, 51, 51))
            magnitude = init_magnitude

        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()