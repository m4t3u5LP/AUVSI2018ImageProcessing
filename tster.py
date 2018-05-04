import cv2 as cv
import numpy as np

img = cv.imread('IMG_0389.png', 0)
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

cv.imshow('ass', img)
