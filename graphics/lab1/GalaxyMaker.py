from math import sin,cos,exp,pi,trunc,sqrt,hypot
from random import random

class Star():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calculate_distance(self,x,y):
        return int(hypot(self.x - x,self.y-y))
    
class GalaxyMaker():

    def __init__(self,width,height):
        self.stars = list()
        self.width = width
        self.height = height

        self._x_center = int(self.width/2)
        self._y_center = int(self.height/2)

        self._rukav_h = self.height
        self._rukav_l = width/10
        
    def _functional_for_mindal(self,x,y):
        a , b = self.width/10 , self.height/5
        p = (x-self._x_center)**2/a**2+(y-self._y_center)**2/b**2
        return exp(-p**1.2)

    def make_mindal_galaxy(self):
        self.stars.clear()
        for x in range(self.width):
            for y in range(self.height):
                if self._functional_for_mindal(x,y) >= random():
                    self.stars.append(Star(x,y))
        return self.stars

    def _functional_for_ellipse(self,x,y):
        point = Star(x,y)
        return exp((-point.calculate_distance(self._x_center,self._y_center)**2.65)/self._rukav_h**2)
    
    def make_ellipse_galaxy(self):
        self.stars.clear()
        for x in range(self.width):
            for y in range(self.height):
                if self._functional_for_ellipse(x,y) >= random():
                    self.stars.append(Star(x,y))
        return self.stars
    
    def _g(self,d,r):
        d *= 0.15
        return exp(-(d**3)/(r**2))
    
    def _functional_for_spiral(self,x,y):
        return self._g((x)**2,self._rukav_l**2)*self._g((y)**2,self._rukav_h**2)     
    
    def _rot(self,x,y,a):
        return int(x*cos(a) + y*sin(a)),int(-x*sin(a) + y*cos(a))
    
    def make_spiral_galaxy(self,arms,alpha):
        self.stars.clear()
        radius = min(self.width,self.height)
        radius = trunc(((radius**2+radius**2)**0.5)/2)
        b = 0.2 * alpha * pi * radius*2 #TODO bind value of slider to second arg
        for x in range(-radius,radius):
            for y in range(-radius,radius):
                if self._functional_for_spiral(x,y) >= random():
                    d = (x*x + y*y)**0.5
                    if d != 0:
                        new_x,new_y = self._rot(x,y,b/d)
                        self.stars.append(Star(new_x+self._x_center,new_y+self._y_center))
        rotation_angle = 2*pi / arms
        for star in self.stars:
            for i in range(arms):
                new_x,new_y = self._rot(x,y,rotation_angle*i)
                self.stars.append(Star(new_x+self._x_center,new_y+self._y_center))
        return self.stars

if __name__ == "__main__" : pass
        
    
