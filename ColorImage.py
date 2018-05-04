import cv2
import numpy as np
from random import *

#colors the given image
#inputs are an image and a number
def color_image(image,colornum0):

    #random pixel BGR values within each color range
    red = [0, 0, 255]#[randint(0, 50), randint(0, 50), randint(205, 255)]
    orange = [0, 113, 255]#[randint(0, 50), randint(78, 178), randint(205, 255)]
    yellow = [0, 255, 255]#[randint(0, 50), randint(205, 255), randint(205, 255)]
    lime = [0, 255, 113]#[randint(0, 50), randint(205, 255), randint(78, 178)]
    green = [0, 255, 0]#[randint(0, 50), randint(205, 255), randint(0, 50)]
    cyan = [255, 255, 0]#[randint(205, 255), randint(205, 255), randint(0, 50)]
    blue = [255, 0, 0]#[randint(205, 255), randint(0, 50), randint(0, 50)]
    magenta = [255, 0, 255]#[randint(205, 255), randint(0, 50), randint(205, 255)]
    purple = [255, 0, 113]#[randint(205, 255), randint(0, 50), randint(78, 178)]
    pink = [113, 0, 255]#[randint(78, 178), randint(0, 50), randint(205, 255)]
    grey = [113, 113, 113]#[randint(78, 178), randint(78, 178), randint(78, 178)]
    black = [10, 10, 10]#[randint(10, 50), randint(10, 50), randint(10, 50)]

    colornum = colornum0
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
    im = image.copy()
    im[np.where((im >= [10, 10, 10]).all(axis=2))] = color
    colornum0 = colornum
    img = im

    #outputs the image with the new color
    return img
