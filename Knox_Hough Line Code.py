import cv2
import numpy as np

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 300, 6, apertureSize=3)
minLineLength = 50
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength, maxLineGap)
for line in lines:
    for x1, y1, x2,y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

print("Number of lines: " + str(len(lines)))
cv2.imshow('houghlines5.jpg', img)
cv2.waitKey(0)