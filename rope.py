from math import *
from calculate import *
from random import *

class rope:
    def __init__(self, xi, yi, xf, yf, length, vx = 0, vy = 0, color = "white", m = 1):
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.length = length
        self.vx = vx
        self.vy = vy
        self.color = color
        self.m = m

    def tick(self, objects, delta_t):
        return 0