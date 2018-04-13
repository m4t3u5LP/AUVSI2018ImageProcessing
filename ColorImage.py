import cv2
import numpy as np
from random import *

#colors the given image
#inputs are an image and a number
def color_image(image,colornum):

    #random pixel BGR values within each color range
    red = [randint(0, 50), randint(0, 50), randint(205, 255)]
    orange = [randint(0, 50), randint(78, 178), randint(205, 255)]
    yellow = [randint(0, 50), randint(205, 255), randint(205, 255)]
    lime = [randint(0, 50), randint(205, 255), randint(78, 178)]
    green = [randint(0, 50), randint(205, 255), randint(0, 50)]
    cyan = [randint(205, 255), randint(205, 255), randint(0, 50)]
    blue = [randint(205, 255), randint(0, 50), randint(0, 50)]
    magenta = [randint(205, 255), randint(0, 50), randint(205, 255)]
    purple = [randint(205, 255), randint(0, 50), randint(78, 178)]
    pink = [randint(78, 178), randint(0, 50), randint(205, 255)]
    grey = [randint(78, 178), randint(78, 178), randint(78, 178)]
    black = [randint(10, 50), randint(10, 50), randint(10, 50)]

    #if statements that assign the variable color to whatever the given number is
    if colornum == 1:
        color = red
    elif colornum == 2:
        color = orange
    elif colornum == 3:
        color = yellow
    elif colornum == 4:
        color = lime
    elif colornum == 5:
        color = green
    elif colornum == 6:
        color = cyan
    elif colornum == 7:
        color = blue
    elif colornum == 8:
        color = magenta
    elif colornum == 9:
        color = purple
    elif colornum == 10:
        color = pink
    elif colornum == 11:
        color = grey
    elif colornum == 12:
        color = black

    #looks at the input image and finds all of the picels that are above [10,10,10]
    #and replaces it with the selected color
    im = image
    im[np.where((im >= [10, 10, 10]).all(axis = 2))] = color

    #outputs the image with the new color
    return im
