from math import *;
G = 0.01
screen_scale = 1

def incrementScreenScale(scale):
    global screen_scale
    screen_scale += scale
    if (screen_scale < 1):
        screen_scale = 1

# Returns the distance between two objects using a variation of the Pythagorean theorem
def get_distance(object_1, object_2):
    return sqrt(((object_1.x - object_2.x) ** 2) + ((object_1.y - object_2.y) ** 2))

# Detects if two objects collide by getting the distance between them and 
# checking if the that distance is less than the sum of their radii.
def detect_collision(object_1, object_2):
    return get_distance(object_1, object_2) < (object_1.radius + object_2.radius)
    
def handle_border_collision(object):
    if (object.x + object.radius > 1 * screen_scale or object.x - object.radius < -1 * screen_scale):
        object.vx *= -1
    if (object.y + object.radius > 1 * screen_scale or object.y - object.radius < -1 * screen_scale):
        object.vy *= -1

def TENSION_handle_border_collision(object):
    if (object.x + object.radius > 1 * screen_scale or object.x - object.radius < -1 * screen_scale):
        object.vx *= -0.8
    if (object.y + object.radius > 1 * screen_scale or object.y - object.radius < -1 * screen_scale):
        object.vy *= -0.8

def map(x, y, width, height):
    return [map_x(x, width), map_y(y, height)]
    
def map_x(x, width):
    return ((x/screen_scale + 1)/2) * width

def map_y(y, height):
    return height - ((y/screen_scale + 1)/2) * height

def map_radius(radius, width):
    return (radius/screen_scale/2) * width

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
        Fx = G * ((object_1.m * object_2.m)/r ** 2) * ndx
        Fy = G * ((object_1.m * object_2.m)/r ** 2) * ndy
        return Fx, Fy

def get_force_of_gravity_of_all_objects(object, objects):
    ΣFx = 0
    ΣFy = 0
    for other_object in objects:
        if (object != other_object):
            a , b = get_force_of_gravity(object, other_object, G)
            ΣFx += a
            ΣFy += b
    return ΣFx, ΣFy

def detect_collision_of_all_objects(object, objects):
    for other_object in objects:
        if object != other_object:
            if detect_collision(object, other_object):
                # Calculate relative velocity
                rel_vel_x = object.vx - other_object.vx
                rel_vel_y = object.vy - other_object.vy

                # Calculate relative distance
                rel_dist_x = object.x - other_object.x
                rel_dist_y = object.y - other_object.y

                # Calculate dot product of relative velocity and relative distance
                dot_product = rel_vel_x * rel_dist_x + rel_vel_y * rel_dist_y

                # Calculate magnitude of the relative distance squared
                rel_dist_squared = rel_dist_x ** 2 + rel_dist_y ** 2

                # Calculate new velocities for conservation of energy and momentum
                object.vx -= 0.99 * (2 * other_object.m / (object.m + other_object.m)) * dot_product / rel_dist_squared * rel_dist_x
                object.vy -= 0.99 * (2 * other_object.m / (object.m + other_object.m)) * dot_product / rel_dist_squared * rel_dist_y

                other_object.vx += 0.99 * (2 * object.m / (object.m + other_object.m)) * dot_product / rel_dist_squared * rel_dist_x
                other_object.vy += 0.99 * (2 * object.m / (object.m + other_object.m)) * dot_product / rel_dist_squared * rel_dist_y

                # Separate the objects to avoid collision
                separation_factor = 0.01  # Adjust this factor as needed
                object.x += rel_dist_x * separation_factor
                object.y += rel_dist_y * separation_factor