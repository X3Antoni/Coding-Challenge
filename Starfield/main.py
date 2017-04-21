import pygame
from star import little_star
from pygame.draw import lines
from pygame.mouse import get_pos
pygame.init()


def remap(x, oldmin, oldmax, newmin, newmax):
    return (x - oldmin) / (oldmax - oldmin) * (newmax - newmin) + newmin


# -------------------- setup the canvas ---------------------------------------

width = 800
height = 800
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Starfield")

# -------------------- create a bunch of stars --------------------------------

stars = []
for i in range(400):
    stars.append(little_star(width, height))

# -------------------- main loop ----------------------------------------------

done = False
while not done:
    # get mouse coordinate
    mouseX, mouseY = get_pos()

    # erase everything on screen into full blackness
    screen.fill((0, 0, 0))

    # draw those stars!!!
    speed = remap(mouseX, 0, size[0], 0, 50)
    for star in stars:
        # update star
        star.update(speed)

        # show star
        sx = remap(star.x / star.z, 0, 1, 0, size[0]) + size[0] / 2
        sy = remap(star.y / star.z, 0, 1, 0, size[1]) + size[1] / 2
        px = remap(star.x / star.pz, 0, 1, 0, size[0]) + size[0] / 2
        py = remap(star.y / star.pz, 0, 1, 0, size[1]) + size[1] / 2
        r = remap(star.z, 0, width, 10, 0)
        star.pz = star.z
        lines(screen, (255, 255, 255), False, [(px, py), (sx, sy)], 1)

    # update the changes on screen
    pygame.display.update()

    # to get out from here!!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
