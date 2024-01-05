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
pygame.display.set_caption("Moving object")
border_collision = False
do_scrolling = True
background_color = (37, 35, 33)
unit_vector_scalar = 500
accuracy = 100
speed = 0.001
physic_step_per_frame = accuracy
delta_t = speed / accuracy
tail_length = 75

# init my objectz with nuffin
objects = [
    # left object
    object(0, 0, 0.005, 0, 0, "yellow", 1000, tail_length),
    # right object
    object(0.7, 0, 0.05, 0, 2, "white", 0.1, tail_length),
    object(-0.25, -0.5, 0.005, 0, -3, "black", 100, tail_length)
]

nomalize_center_of_masses(objects)

def draw():
    screen.fill(background_color)

    for object in objects:
        object.add_tail(width, height)
        if (len(object.tail) > 2):
            pygame.draw.lines(screen, "red", False, object.tail, 1)

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

        elif event.type == pygame.MOUSEWHEEL and do_scrolling:
            incrementScreenScale(event.y)

    draw()
    for _ in range(physic_step_per_frame):
        tick()