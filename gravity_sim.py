import pygame
import sys
from object import *
from random import *
from calculate import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity")
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

objects = generate_random_objects(2)

nomalize_center_of_masses(objects)

def draw():
    screen.fill(background_color)

    for object in objects:
        # object.add_tail(width, height)
        # if (len(object.tail) > 2):
        #     pygame.draw.lines(screen, "red", False, [map(x, y, width, height) for x , y in object.tail], 1)

        # Draw the object
        pygame.draw.circle(screen, object.color, (map_x(object.x, width), map_y(object.y, height)), map_radius(object.radius, width))    

    pygame.display.flip()
    pygame.time.Clock().tick(60)

def tick():
    for object in objects:
        get_force_of_gravity_of_all_objects(object, objects)
        detect_collision_of_all_objects(object, objects)
        if (border_collision):
            handle_border_collision(object)

        object.tick(objects, delta_t)

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