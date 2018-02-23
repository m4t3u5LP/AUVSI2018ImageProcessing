import cv2
import numpy as np


def detect_shape(image):
    # load the image
    img = cv2.imread(image)

    # Blur the image
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Gray the image
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    thresh1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]
    thresh2 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]

    # erode image
    kernel = np.ones((5, 5), np.uint8)
    erosion1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    kernel2 = np.ones((20, 20), np.uint8)
    erosion2 = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel2)

    # find contours
    im2, contours1, hierarchy = cv2.findContours(erosion1, 1, 2)
    cnt = contours1[0]
    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)
    return cnt, img


def detect(c):
    shape = "Original"
    peri = cv2.arcLength(c, True)
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    print("Perimeter: " + str(peri))
    print("Lines: " + str(len(approx)))
    if len(approx) == 3:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print("Aspect Ratio: " + str(ar))
        shape = "triangle"

    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        print("Aspect Ratio: " + str(ar))

    elif len(approx) == 5:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "pentagon" if ar <= 1.5 else "half circle"
        print("Aspect Ratio: " + str(ar))

    elif len(approx) == 6:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print("Aspect Ratio: " + str(ar))
        shape = "hexagon"

    elif len(approx) == 7:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print(ar)
        shape = "heptagon"

    elif len(approx) == 8:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print("Aspect Ratio: " + str(ar))
        shape = "octogon"

    elif len(approx) == 12:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print("Aspect Ratio: " + str(ar))
        shape = "cross"

    elif len(approx) == 10:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        print("Aspect Ratio: " + str(ar))
        shape = "star"
    else:
        shape = "circle"

    return shape

print(detect(detect_shape("Quarter Circle.png")[0]))

cv2.imshow('s', detect_shape("")[1])
cv2.waitKey(0)