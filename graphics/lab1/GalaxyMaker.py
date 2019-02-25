from math import sin,cos,exp,pi,trunc
from random import random

class Star():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # if __name__ = "__main__" : pass


class GalaxyMaker():

    def __init__(self,width,height):
        self.stars = list()
        self.width = width
        self.height = height

        self._x_center = int(self.width/2)
        self._y_center = int(self.height/2)

        self._rukav_h = self.height
        self._rukav_l = 25
        
    def _functional(self,d,r,galaxy_type):
        if galaxy_type == 0:
            pass
        elif galaxy_type == 1: 
            pass
        elif galaxy_type == 2:
            return exp(-(d**2.5)/(r**2))

    
    def _g(self,x,y):
        galaxy_type = 2 # spiral galaxy id
        return self._functional((x)**2,self._rukav_l**2,galaxy_type)*self._functional((y)**2,self._rukav_h**2,galaxy_type)
    
    def _rot(self,x,y,a):
        return int(x*cos(a) + y*sin(a)),int(-x*sin(a) + y*cos(a))
    
    def make_spiral_galaxy(self,arms,alpha):
        radius = min(self.width,self.height)
        radius = trunc(((radius**2+radius**2)**0.5)/2)
        b = 0.2 * alpha * pi * radius*2 #TODO bind value of slider to second arg
        for x in range(-radius,radius):
            for y in range(-radius,radius):
                if self._g(x,y) >= random():
                    d = (x*x + y*y)**0.5
                    if d != 0:
                        new_x,new_y = self._rot(x,y,b/d)
                        self.stars.append(Star(new_x+self._x_center,new_y+self._y_center))
                        new_x,new_y = self._rot(new_x,new_y,pi / arms)
                        self.stars.append(Star(new_x+self._x_center,new_y+self._y_center))

if __name__ == "__main__" : pass
        
    
