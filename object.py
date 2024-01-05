from math import *
from physics import *

class Object:
    def __init__(self, x, y, radius, vx = 0, vy = 0, color = "white", m = 1):
        self.x = x
        self.y = y
        self.radius = radius * sqrt(m)
        self.vx = vx
        self.vy = vy
        self.color = color
        self.m = m

    def tick(self, delta_t):
        Fx, Fy = detect_collision_of_all_objects(self)
        # update velocity with the force
        self.vx += 0.5 * delta_t * (Fx / self.m)
        self.vy += 0.5 * delta_t * (Fy / self.m)
        # update the position with velocity
        self.x += delta_t * self.vx
        self.y += delta_t * self.vy
        Fx, Fy = detect_collision_of_all_objects(self)
        # update velocity with new force
        self.vx += 0.5 * delta_t * (Fx / self.m)
        self.vy += 0.5 * delta_t * (Fy / self.m)