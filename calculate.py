from math import *;

# Returns the distance between two objects using a variation of the Pythagorean theorem
def get_distance(object_1, object_2):
    return sqrt(((object_1.x - object_2.x) ** 2) + ((object_1.y - object_2.y) ** 2))

# Detects if two objects collide by getting the distance between them and 
# checking if the that distance is less than the sum of their radii.
def detect_collision(object_1, object_2):
    if (get_distance(object_1, object_2) < (object_1.radius + object_2.radius)):
        return True
    else:
        return False
    
def handle_border_collision(object):
    if (object.x + object.radius > 1 or object.x - object.radius < -1):
        object.vx *= -1
    if (object.y + object.radius > 1 or object.y - object.radius < -1):
        object.vy *= -1
    
def map_x(x, width):
    return ((x + 1)/2) * width

def map_y(y, height):
    return height - ((y + 1)/2) * height

def map_radius(radius, width):
    return (radius/2) * width

def nomalize_center_of_masses(objects):
    Σx, Σy, Σvx, Σvy, Σm = 0, 0, 0, 0, 0

    for object in objects:
        Σx += object.x * object.m
        Σy += object.y * object.m
        Σvx += object.vx * object.m
        Σvy += object.vy * object.m
        Σm += object.m

        Σx = Σx / Σm
        Σy = Σy / Σm
        Σvx = Σvx / Σm
        Σvy = Σvy / Σm

        for object in objects:
            object.x -= Σx
            object.y -= Σy
            object.vx -= Σvx
            object.vy -= Σvy

def get_force_of_gravity(object_1, object_2, G):
        r = get_distance(object_1, object_2)
        # get normalized direction
        ndx = -(object_1.x - object_2.x) / r
        ndy = -(object_1.y - object_2.y) / r
        Fx = G * ((object_1.m * object_2.m)/r ** 1) * ndx
        Fy = G * ((object_1.m * object_2.m)/r ** 1) * ndy
        return Fx, Fy