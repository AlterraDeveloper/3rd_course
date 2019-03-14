from random import random
from math import exp

from GalaxyMaker import GalaxyMaker, Star

class EllipseGalaxy(GalaxyMaker):
    def __init__(self,width,height, radius_ratio):
        GalaxyMaker.__init__(self,width,height)
        self.ratio = radius_ratio

    def _functional(self, x, y):
        point = Star(x, y)
        return exp((-point.calculate_distance(0, 0) ** 2.75) / (self._rukav_h ** 2 * self.ratio))

    def make(self):
        self.stars.clear()
        for x in range(int(-self.width / 2), int(self.width / 2)):
            for y in range(int(-self.height / 2), int(self.height / 2)):
                if self._functional(x, y) >= random():
                    self.stars.append(Star(x, y))
        return self.stars

if __name__ == "__main__": pass