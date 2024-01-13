import pygame
import sys
from hanging_object import *
from rope import *
from random import *
from calculate import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tension")
border_collision = True
do_scrolling = True
background_color = (37, 35, 33)
# unit_vector_scalar = 500
# accuracy = 500
# speed = 1
tick_rate = 20
delta_t = 0.001 # / accuracy
tail_length = 50
# e = 2.718281828

hobjects = [hObject(0, 0, 0.5, 0, 0)]
# rope = rope()

def draw():
    screen.fill(background_color)

    for hobject in hobjects:
        pygame.draw.circle(screen, hobject.color, (map_x(hobject.x, width), map_y(hobject.y, height)), map_radius(hobject.radius, width))    

    pygame.display.flip()
    pygame.time.Clock().tick(60)

def tick():
    for hobject in hobjects:
        if (border_collision):
            TENSION_handle_border_collision(hobject)

        hobject.tick(delta_t)
    
    # for rope in ropes:

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # elif event.type == pygame.MOUSEWHEEL and do_scrolling:
        #     mods = pygame.key.get_mods()
        #     if mods & pygame.KMOD_SHIFT:
        #         print(speed)
        #         speed *= 0.5 + (1 / (1 + e ** -event.y))
        #         delta_t = speed / accuracy
        #     elif mods & pygame.KMOD_CTRL:
        #         print(accuracy)
        #         accuracy *= 0.5 + (1 / (1 + e ** -event.y))
        #         physic_step_per_frame = min(1, accuracy)
        #         delta_t = speed / accuracy
        #     else:
        #         print("zoom")
        #         incrementScreenScale(-event.y)

    draw()
    for _ in range(tick_rate):
        tick()