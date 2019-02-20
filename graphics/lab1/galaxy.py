from math import *
import random
import pprint
import numpy as np
from skimage.io import imread,imsave

# background = imread('galaxy_original.png')
background = imread('space_bg.jpg')
rows = background.shape[0]
columns = background.shape[1]

x_center = int(rows/2)
y_center = int(columns/2)

rukav_h = columns
rukav_l = 25

def functional(d,r):
    d *= 0.15
    return exp(-(d*d*d)/(r*r))

def g(x,y):
    return functional((x)**2,rukav_l**2)*functional((y)**2,rukav_h**2)

def rot(x,y,a):
    return int(x*cos(a) + y*sin(a)),int(-x*sin(a) + y*cos(a))

def rotateWithMatrix(x_old,y_old,angle):
    R = [ [ np.cos(radians(angle)), -np.sin(radians(angle)) ], [ np.sin(radians(angle)), np.cos(radians(angle)) ] ]
    [new_x,new_y] = np.dot([x_old, y_old], R)
    return trunc(new_x),trunc(new_y)

radius = min(rows,columns)

arms = 4

offsets = [pi/(i+1) for i in range(arms)]
radius = trunc(((radius**2+radius**2)**0.5)/2)
b = 0.2 * 0.5*pi * radius*2 #TODO bind value of slider to second arg
for x in range(-radius,radius):
    for y in range(-radius,radius):
        if g(x,y) >= random.random():
            d = (x*x + y*y)**0.5
            if d != 0:
                new_x,new_y = rot(x,y,b/d)
                background[new_x+x_center,new_y+y_center] = [0+d/2,0,255-d]
                for angle in offsets:
                    new_x,new_y = rot(new_x,new_y,pi / arms)
                    background[new_x+x_center,new_y+y_center] = [0+d/2,0,255-d]
imsave("galaxy.png",background)
