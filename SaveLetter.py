import cv2
import os

#C:\Users\knoxborges\PycharmProjects\AUVSI\ImageRec\Results\Shapes
#C:\Users\knoxborges\PycharmProjects\AUVSI\ImageRec\Results\Letters

def save_letter(NumFields, NumShapes, NumLetters, NumColors1, NumColors2):

    A = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\A"
    B = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\B"
    C = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\C"
    D = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\D"
    E = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\E"
    F = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\F"
    G = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\G"
    H = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\H"
    I = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\I"
    J = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\J"
    K = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\K"
    L = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\L"
    M = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\M"
    N = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\N"
    O = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\O"
    P = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\P"
    Q = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\Q"
    R = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\R"
    S = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\S"
    T = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\T"
    U = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\U"
    V = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\V"
    W = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\W"
    X = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\X"
    Y = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\Y"
    Z = "C:\\Users\\knoxborges\\PycharmProjects\\AUVSI\\ImageRec\\Results\\Letters\\Z"

    filename = 'field%s_shape%s_letter%s_lettercolor%s_shapecolor%s.png'%(NumFields, NumShapes, NumLetters, NumColors1, NumColors2)

    if NumLetters == 0:
        path = A
    elif NumLetters == 1:
        path = B
    elif NumLetters == 2:
        path = C
    elif NumLetters == 3:
        path = D
    elif NumLetters == 4:
        path = E
    elif NumLetters == 5:
        path = F
    elif NumLetters == 6:
        path = G
    elif NumLetters == 7:
        path = H
    elif NumLetters == 8:
        path = I
    elif NumLetters == 9:
        path = J
    elif NumLetters == 10:
        path = K
    elif NumLetters == 11:
        path = L
    elif NumLetters == 12:
        path = M
    elif NumLetters == 13:
        path = N
    elif NumLetters == 14:
        path = O
    elif NumLetters == 15:
        path = P
    elif NumLetters == 16:
        path = Q
    elif NumLetters == 17:
        path = R
    elif NumLetters == 18:
        path = S
    elif NumLetters == 19:
        path = T
    elif NumLetters == 20:
        path = U
    elif NumLetters == 21:
        path = V
    elif NumLetters == 22:
        path = W
    elif NumLetters == 23:
        path = X
    elif NumLetters == 24:
        path = Y
    elif NumLetters == 25:
        path = Z


    savefile = os.path.join(path,filename)

    return savefile


img = cv2.imread('1.png')
file = save_letter(0, 0, 3, 1, 2)
cv2.imwrite(file, img)
