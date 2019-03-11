from math import sin,cos,exp,pi,trunc,sqrt,hypot
from random import random

class Star():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calculate_distance(self,x,y):
        return abs(int(hypot(self.x,self.y)))
    
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
        a , b = self.width/4 , self.height/8
        p = (x)**2/a**2+(y)**2/b**2
        return exp(-p**3)

    def make_mindal_galaxy(self):
        self.stars.clear()
        for x in range(int(-self.width/2),int(self.width/2)):
            for y in range(int(-self.height/2),int(self.height/2)):
                if self._functional_for_mindal(x,y) >= random():
                    new_x,new_y = self._rot(x,y,-pi/4)
                    self.stars.append(Star(new_x,new_y))
        return self.stars

    def _functional_for_ellipse(self,x,y,ratio):
        point = Star(x,y)
        return exp((-point.calculate_distance(0,0)**2.75)/(self._rukav_h**2*ratio))
    
    def make_ellipse_galaxy(self,ratio):
        self.stars.clear()
        for x in range(int(-self.width/2),int(self.width/2)):
            for y in range(int(-self.height/2),int(self.height/2)):
                if self._functional_for_ellipse(x,y,ratio) >= random():
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
                        self.stars.append(Star(new_x,new_y))                            
        rotation_angle = pi / arms
        stars_copy = self.stars.copy()
        for star in stars_copy:
            for i in range(1,arms):
                new_x,new_y = self._rot(star.x,star.y,rotation_angle*i)
                self.stars.append(Star(new_x,new_y))
        return self.stars

if __name__ == "__main__" : pass
        
    
