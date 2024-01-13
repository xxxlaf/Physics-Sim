from math import *
from calculate import *
from random import *

class hObject:
    def __init__(self, x, y, radius, vx = 0, vy = 0, color = "white", m = 1):
        self.x = x
        self.y = y
        self.radius = radius * sqrt(m)
        self.vx = vx
        self.vy = vy
        self.color = color
        self.m = m
        self.previous_vy_sign = 1  # Initialize with positive sign

    def tick(self, delta_t):
        # apply_gravity(self, 1000, delta_t)
        self.vy -= (9.8 / 1000) * delta_t
        self.y += self.vy
        print(self.vy)

        # Check if velocity changes sign more than once consecutively
        current_vy_sign = 1 if self.vy >= 0 else -1
        if current_vy_sign != self.previous_vy_sign:
            if abs(self.vy) < 0.01:  # Threshold to consider as almost zero velocity
                self.vy = 0  # Set velocity to zero to stop bouncing
        
        # Update previous velocity sign for the next iteration
        self.previous_vy_sign = current_vy_sign
        

# def apply_gravity(hobject, a, delta_t):
    # hobject.vy += a * delta_t