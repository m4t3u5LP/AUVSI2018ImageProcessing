import cv2
from random import *
import numpy as np
from ColorImage import color_image

#function that puts a shape and a letter on a field
#inputs an image of a field, shape, letter, number for color1, number for color2
def CreateImage(field, shape, letter, letter_color, shape_color):

    #assigns input images to variables img1-3
    img1 = field
    img2 = shape
    img3 = letter

    #runs the color_image function to change the color of the shape and letter
    img2 = color_image(img2, shape_color)
    img3 = color_image(img3, letter_color)

    #selects a random point on the input field image to place the letter and shape
    x = randint(0, 317)
    y = randint(0, 526)
    #creates a boundary from the edge of the picture so the images wont get cutoff
    x2 = x + 100
    y2 = y + 100

    # puts shape on picture (img2)
    rows, cols, channels = img2.shape
    roi = img1[x:x2, y:y2]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    img1[x:x2, y:y2] = dst

    # puts letter on image (img3)
    rows, cols, channels = img3.shape
    roi = img1[x:x2, y:y2]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img3_fg)
    img1[x:x2, y:y2] = dst

    #outputs the generated image with the colored letters and shpaes on a field
    return img1
