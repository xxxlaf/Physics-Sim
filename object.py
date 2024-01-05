from math import *
from calculate import *

class object:
    def __init__(self, x, y, radius, vx = 0, vy = 0, color = "white", m = 1, max_tail_length = 15):
        self.x = x
        self.y = y
        self.radius = radius * sqrt(m)
        self.vx = vx
        self.vy = vy
        self.color = color
        self.m = m
        self.tail = []
        self.max_tail_length = max_tail_length

    def tick(self, objects, delta_t):
        Fx, Fy = get_force_of_gravity_of_all_objects(self, objects)
        # update velocity with the force
        self.vx += 0.5 * delta_t * (Fx / self.m)
        self.vy += 0.5 * delta_t * (Fy / self.m)
        # update the position with velocity
        self.x += delta_t * self.vx
        self.y += delta_t * self.vy
        Fx, Fy = get_force_of_gravity_of_all_objects(self, objects)
        # update velocity with new force
        self.vx += 0.5 * delta_t * (Fx / self.m)
        self.vy += 0.5 * delta_t * (Fy / self.m)

    def add_tail(self, width, height):
        self.tail.append([map_x(self.x, width), map_y(self.y, height)])
        if (len(self.tail) > self.max_tail_length and len(self.tail) > 0):
            self.tail.pop(0)
        