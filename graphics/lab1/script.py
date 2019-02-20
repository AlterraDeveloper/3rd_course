from math import *
import random
import pprint
import numpy as np
# import matplotlib
from skimage.io import imread,imsave


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

ROWS = 0
COLUMNS = 1
background = imread('galaxy_original.png')
# background = imread('stars_on_sky.jpg')
image_size = background.shape

rukav_l = min(image_size[ROWS],image_size[COLUMNS])
rukav_h = 20

x_center = image_size[ROWS]/2
y_center = image_size[COLUMNS]/2

def functional(d,r):
    d *= 0.15
    return exp(-(d*d*d)/(r*r))

def g(x,y):
    return functional((x - 200)**2,rukav_l**2)*functional((y-200)**2,rukav_h**2)

def rotateWithMatrix(x_old,y_old,angle):
    R = [ [ np.cos(radians(angle)), -np.sin(radians(angle)) ], [ np.sin(radians(angle)), np.cos(radians(angle)) ] ]
    [new_x,new_y] = np.dot([x_old, y_old], R)
    return trunc(new_x),trunc(new_y)

def rot(x,y,a):
    # return Point(trunc(x*cos(radians(a)) + y*sin(radians(a))),trunc(-x*sin(radians(a)) + y*cos(radians(a))))
    return trunc(x*cos(a) + y*sin(a)),trunc(-x*sin(a) + y*cos(a))


b = pi *0.2 * rukav_l
# radius = trunc(((rukav_l**2+rukav_l**2)**0.5)/2)
# stars = []
# for x in range(-radius,radius):
#     for y in range(-radius,radius):
#         if g(x,y) >= random.random():
#             d = (x**2+y**2)**0.5
#             stars.append(rot(x,y,b/d))
# arms = 2
# al = 2*pi / arms
# for p in stars:
#     for i in range(arms):
#         stars.append(rot(p.x,p.y,al*i))

# for star in stars:
    # background[star.x,star.y] = 255

for row in range(400):
    for column in range(400):
        if g(row+1,column+1) >= random.random():
            # background[new_row,new_column] = 255
            d = ((row-200)**2 + (column-200)**2)**0.5
            row,column = rot(row,column,b/d**0.1)
            if row < 400 and column < 400:
                background[row,column] = 255
                new_row,new_column = rotateWithMatrix(row,column,450)
                background[new_row,new_column] = 255
#
#
#             background[row,column] = 255
#
#             # d = sqrt( (row-x_center)**2 + (column-y_center)**2 )
#             new_row,new_column = rotateWithMatrix(row,column,-450)
#             background[new_row,new_column] = 255
#             # new_row,new_column = rotate(row,column)
#             # background[new_row,new_column] = [255,0,255]

imsave('galaxy.png',background)


















# def newRotate(x_old,y_old):
#     delta = 0.2 * pi * rukav_l/2
#     d = sqrt( (x_old)**2 + (y_old)**2 )
#     alpha = delta / d**0.5
#     x_new = x_old*cos(radians(alpha)) + y_old*sin(radians(alpha))
#     y_new = -x_old*sin(radians(alpha)) + y_old*cos(radians(alpha))
#     return trunc(x_new),trunc(y_new)
# def rotate(x_old,y_old):
#     delta = 0.2 * pi * rukav_l/2
#     d = sqrt( (x_old-x_center)**2 + (y_old-y_center)**2 )
#     if d != 0:
#          alpha = delta / d**0.1
#          R = [ [ np.cos(radians(alpha)), -np.sin(radians(alpha)) ], [ np.sin(radians(alpha)), np.cos(radians(alpha)) ] ]
#          [new_x,new_y] = np.dot([x_old, y_old], R)
#          # print(alpha)
#          return trunc(x_center+fabs(new_x)),trunc(y_center+fabs(new_y))
#
#          # if angle == 0: angle = math.degrees(alpha)
#
#          # new_x = x_center + new_x
#          # new_y = y_center + new_y
#          # new_x = math.trunc(new_x)
#          # new_y = math.trunc(new_y)
#          # if not (new_x >= image_size[ROWS] and new_y >= image_size[COLUMNS]):
#          # return math.trunc(new_x),math.trunc(new_y)
#     return x_old,y_old
#     # delta = 0.2 * math.pi * rukav_l/2
#     # d = math.sqrt( (x-x_center)**2 + (y-y_center)**2 )
#     # if d != 0:
#          # alpha = delta / d**0.25
#          # x = math.exp(0.6)
#          # x =  x*math.cos(alpha)-y*math.sin(alpha)
#          # y =  x*math.sin(alpha)+y*math.cos(alpha)
#          # if y > y_center:
#              # x = x - d*math.sin(math.radians(alpha))
#              # y = y + d*math.cos(math.radians(alpha))
#              # x = x - d*math.sin(alpha+math.pi)
#              # y = y + d*math.cos(alpha+math.pi)
#          # else:
#              # x = x + d*math.sin(math.radians(alpha))
#              # y = y - d*math.cos(math.radians(alpha))
#              # x = x + d*math.sin(alpha+math.pi)
#              # y = y - d*math.cos(alpha+math.pi)
#     # return math.trunc(x),math.trunc(y)
