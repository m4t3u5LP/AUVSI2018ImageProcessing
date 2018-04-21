import cv2
import os

#C:\Users\knoxborges\PycharmProjects\AUVSI\ImageRec\Results\Shapes
#C:\Users\knoxborges\PycharmProjects\AUVSI\ImageRec\Results\Letters

def save_shape(NumFields, NumShapes, NumLetters, NumColors1, NumColors2):

    circle = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Circle"
    cross = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Cross"
    diamond = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Diamond"
    heptagon = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Heptagon"
    hexagon = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Hexagon"
    octagon = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Octagon"
    pentagon = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Pentagon"
    quartercircle = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Quarter-Circle"
    rectangle = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Rectangle"
    semicircle = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Semi-Circle"
    square = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Square"
    star = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Star"
    trapezoid = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Trapezoid"
    triangle = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Shapes\\Triangle"

    filename = 'field%s_shape%s_letter%s_lettercolor%s_shapecolor%s.png'%(NumFields, NumShapes, NumLetters, NumColors1, NumColors2)

    if NumShapes == 0:
        path = circle
    if NumShapes == 1:
        path = cross
    elif NumShapes == 2:
        path = diamond
    elif NumShapes == 3:
        path = heptagon
    elif NumShapes == 4:
        path = hexagon
    elif NumShapes == 5:
        path = octagon
    elif NumShapes == 6:
        path = pentagon
    elif NumShapes == 7:
        path = quartercircle
    elif NumShapes == 8:
        path = rectangle
    elif NumShapes == 9:
        path = semicircle
    elif NumShapes == 10:
        path = square
    elif NumShapes == 11:
        path = star
    elif NumShapes == 12:
        path = trapezoid
    elif NumShapes == 13:
        path = triangle

    savefile = os.path.join(path,filename)

    return savefile


#img = cv2.imread('1.png')
#file = save_shape(0, 3, 0, 1, 2)
#print(file)
#cv2.imwrite(file, img)
