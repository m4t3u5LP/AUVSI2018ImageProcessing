import cv2
from random import *
import numpy as np
from ColorImage import color_image
import math

#function that puts a shape and a letter on a field
#inputs an image of a field, shape, letter, number for color1, number for color2
def CreateImage(field, shape, letter, letter_color, shape_color):

    #assigns input images to variables img1-3
    img1 = field
    oimg2 = shape
    oimg3 = letter

    #runs the color_image function to change the color of the shape and letter
    img2 = color_image(oimg2, shape_color)
    img3 = color_image(oimg3, letter_color)

    shapesize = img2.shape[:2] #height by width
    fieldsize = img1.shape[:2]

    imagebounds1 = fieldsize[0] - shapesize[0]
    imagebounds2 = fieldsize[1] - shapesize[1]


    #selects a random point on the input field image to place the letter and shape
    x = randint(0, imagebounds1)
    y = randint(0, imagebounds2)
    #creates a boundary from the edge of the picture so the images wont get cutoff
    x2 = x + shapesize[0]
    y2 = y + shapesize[1]

    vis = img1.copy()
    vis2 = img2.copy()
    vis3 = img3.copy()
    # puts shape on picture (img2)
    rows, cols, channels = vis2.shape
    roi = vis[x:x2, y:y2]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(vis2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(vis2, img2, mask=mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    vis[x:x2, y:y2] = dst

    # puts letter on image (img3)
    rows, cols, channels = vis3.shape
    roi = vis[x:x2, y:y2]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(vis3, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img3_fg = cv2.bitwise_and(vis3, vis3, mask=mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img3_fg)
    vis[x:x2, y:y2] = dst

    img1 = vis
    img2 = vis2
    img3 = vis3

    #outputs the generated image with the colored letters and shpaes on a field
    return img1
