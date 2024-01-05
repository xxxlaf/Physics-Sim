import pygame
import sys
from object import *;
from random import *;
from calculate import *;

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

# init my objectz with nuffin
objects = [
    # left object
    object(-0.5, 0, 0.05, 0.05, -0.05, "white", 1),
    # right object
    object(0.5, 0, 0.05, -0.05, 0.05, "white", 1)
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

        # Draw force vector (red line)
        force_vector = (object.vx * unit_vector_scalar, object.vy * unit_vector_scalar)
        pygame.draw.line(screen, (255, 0, 0), (map_x(object.x, width), map_y(object.y, height)), 
                         (map_x(object.x, width) + force_vector[0], map_y(object.y, height) + force_vector[1]), 2)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    return 0

def tick():
    for object in objects:
        ΣFx = 0
        ΣFy = 0
        for object_2 in objects:
            if (object != object_2):
                a , b = get_force_of_gravity(object, object_2, G)
                ΣFx += a
                ΣFy += b
                if (detect_collision(object, object_2)):
                    object.vx *= -1
                    object.vy *= -1
        if (border_collision):
            handle_border_collision(object)

        object.tick(ΣFx , ΣFy, 0.1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    tick()