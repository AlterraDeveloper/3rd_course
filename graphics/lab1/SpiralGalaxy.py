from random import random
from math import sin, cos, exp, pi, trunc, sqrt, hypot

from GalaxyMaker import GalaxyMaker, Star

class SpiralGalaxy(GalaxyMaker):

    def __init__(self,width,height , arms, alpha):
        GalaxyMaker.__init__(self,width,height)
        self.arms = arms
        self.alpha = alpha    		

    def _g(self, d, r):
        d *= 0.15
        return exp(-(d ** 3) / (r ** 2))

    def _functional(self, x, y):
        return self._g((x) ** 2, self._rukav_l ** 2) * self._g((y) ** 2, self._rukav_h ** 2)

    def make(self):
        self.stars.clear()
        radius = min(self.width, self.height)
        radius = trunc(((radius ** 2 + radius ** 2) ** 0.5) / 2)
        b = 0.2 * self.alpha * pi * radius * 2
        for x in range(-radius, radius):
            for y in range(-radius, radius):
                if self._functional(x, y) >= random():
                    d = (x * x + y * y) ** 0.5
                    if d != 0:
                        new_x, new_y = self._rot(x, y, b / d)
                        self.stars.append(Star(new_x, new_y))
        rotation_angle = pi / self.arms
        stars_copy = self.stars.copy()
        for star in stars_copy:
            for i in range(1, self.arms):
                new_x, new_y = self._rot(star.x, star.y, rotation_angle * i)
                self.stars.append(Star(new_x, new_y))
        return self.stars

if __name__ == "__main__": pass