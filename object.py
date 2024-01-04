from math import *;

class object:
    def __init__(self, x, y, radius, vx = 0, vy = 0, color = "white", m = 1):
        self.x = x
        self.y = y
        self.radius = radius * sqrt(m)
        self.vx = vx
        self.vy = vy
        self.color = color
        self.m = m
    
    def tick(self, Fx, Fy, delta_t):
        self.x += self.vx * delta_t
        self.y += self.vy * delta_t
        self.vx += self.m * Fx * delta_t
        self.vy += self.m * Fy * delta_t