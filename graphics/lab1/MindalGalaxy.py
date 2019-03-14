from random import random
from math import exp,pi

from GalaxyMaker import GalaxyMaker, Star

class MindalGalaxy(GalaxyMaker):
    def __init__(self,width,height, a, b):
        GalaxyMaker.__init__(self,width,height)
        self.a = a
        self.b = b

    def _functional(self, x, y):
        _a, _b = self.width / self.a, self.height / self.b
        p = (x) ** 2 / _a ** 2 + (y) ** 2 / _b ** 2
        return exp(-p ** 3)

    def make(self):
        self.stars.clear()
        for x in range(int(-self.width / 2), int(self.width / 2)):
            for y in range(int(-self.height / 2), int(self.height / 2)):
                if self._functional(x, y) >= random():
                    new_x, new_y = self._rot(x, y, -pi / 4)
                    self.stars.append(Star(new_x, new_y))
        return self.stars

if __name__ == "__main__": pass