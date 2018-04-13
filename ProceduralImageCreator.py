from ImageCreatorFunction import CreateImage
import os
from os.path import isfile, join
import numpy
import cv2
from random import *

#Folders are needed for pictures of fields, shapes, and letters
ourfield = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Fields\\grass.jpg"#"C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\Diamond1.jpg"
ourshape = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Shapes\\star.png"
ourletter = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Letters\\K.png"


fieldpath = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Fields"
shapepath = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Shapes"
letterpath = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Letters"

#function that makes an image with the shape, and letter with random colors onto the field
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#draws images from the folders
images1 = load_images_from_folder(fieldpath)
images2 = load_images_from_folder(shapepath)
images3 = load_images_from_folder(letterpath)

#creates random numbers due to how many pictures are in your folders
#this is for the 9 shapes
A = randint(0,9)
#this is for the 26 letters
B = randint(0,25)
#this is for the 12 colors
C = randint(1,12)
D = randint(1,12)

#calls the function that creates the image
GeneratedImage = CreateImage(images1[0], images2[A], images3[B], C, D)

#shows the generated image in a window
cv2.imshow('res', GeneratedImage)
cv2.waitKey(0)  ## Wait for keystroke
cv2.destroyAllWindows()  ## Destroy all windows
