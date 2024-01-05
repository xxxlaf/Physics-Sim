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
border_collision = True
background_color = (37, 35, 33)
G = 0.01
unit_vector_scalar = 500
accuracy = 2500
speed = 0.1
physic_step_per_frame = accuracy
delta_t = speed / accuracy

# init my objectz with nuffin
objects = [
    # left object
    Object(-0.5, 0, 0.05, 0, -0.05, "white", 1),
    # right object
    Object(0.5, 0, 0.05, 0, 0.05, "white", 1)
]

# fill my objectz with objects
# for i in range(2):
#     objects.append(object(uniform(-1, 1), uniform(-1, 1), 0.05, 0.05, 0.05, "white", 1))

# nomalize_center_of_masses(objects)

def draw():
    screen.fill(background_color)

    for object in objects:
        # Draw the object
        pygame.draw.circle(screen, object.color, (map_x(object.x, width), map_y(object.y, height)), map_radius(object.radius, width))    

        # Draw velocity vector (red line)
        vel_vector = (object.vx * unit_vector_scalar, object.vy * unit_vector_scalar)
        pygame.draw.line(screen, (255, 0, 0), (map_x(object.x, width), map_y(object.y, height)), 
                         (map_x(object.x, width) + vel_vector[0], map_y(object.y, height) - vel_vector[1]), 2)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    return 0

def get_force_of_gravity_of_all_objects(object):
    ΣFx = 0
    ΣFy = 0
    for other_object in objects:
        if (object != other_object):
            a , b = get_force_of_gravity(object, other_object, G)
            ΣFx += a
            ΣFy += b
    return ΣFx, ΣFy

def detect_collision_of_all_objects(object):
    for other_object in objects:
        if (object != other_object):
            if (detect_collision(object, other_object)):
                object.vx *= -1
                object.vy *= -1

def tick():
    for object in objects:
        get_force_of_gravity_of_all_objects(object)
        detect_collision_of_all_objects(object)
        if (border_collision):
            handle_border_collision(object)

        object.tick(delta_t)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    for _ in range(physic_step_per_frame):
        tick()