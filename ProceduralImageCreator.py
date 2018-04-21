from ImageCreatorFunction import CreateImage
from SaveShape import save_shape
from SaveLetter import save_letter
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
NumShapes = 2#14#randint(0,9)
#this is for the 26 letters
NumLetters = 2#26#randint(0,25)
#this is for the 12 colors
NumFields = 1#randint(1,12)
NumColors1 = 3#12#randint(1,12)
NumColors2 = 3#12#randint(1,12)

c = 0
GeneratedImage = []
#calls the function that creates the image
for i in range(0, NumFields):
    for j in range(0,NumShapes):
        for k in range(0, NumLetters):
            for u in range(1, NumColors1):
                for v in range(1, NumColors2):
                    if u != v:
                        GeneratedImage.append(CreateImage(images1[i], images2[j], images3[k], u, v))
                        shapepath = save_shape(i, j, k, u, v)
                        cv2.imwrite(shapepath, GeneratedImage[c])
                        letterpath = save_letter(i, j, k, u, v)
                        cv2.imwrite(letterpath, GeneratedImage[c])


#shows the generated image in a window
                        #cv2.imshow('%s'%c, GeneratedImage[c])
                        #cv2.waitKey(0)  ## Wait for keystroke
                        cv2.destroyAllWindows()  ## Destroy all windows
                        c = c + 1