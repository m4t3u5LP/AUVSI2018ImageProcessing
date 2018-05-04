import cv2
import label_image

# Create MSER object
mser = cv2.MSER_create()

# Your image path i-e receipt path
img = cv2.imread('images/IMG_0386.png')

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

vis = img.copy()

# detect regions in gray scale image
regions, _ = mser.detectRegions(gray)

hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

plswrk = []

for contour in hulls:
    x, y, w, h = cv2.boundingRect(contour)
    plswrk.append([x, y, w, h])

gunnawrk = []
for i in range(0, len(plswrk) - 1):
    xDiff = (plswrk[i][0] - plswrk[i + 1][0]) / plswrk[i][0]
    yDiff = (plswrk[i][1] - plswrk[i + 1][1]) / plswrk[i][1]
    pDiff = ((xDiff ** 2) + (yDiff ** 2)) ** 0.5
    if pDiff >= 0.5:
        gunnawrk.append(plswrk[i])
c = 0
for i in gunnawrk:
    crop_img = vis[i[1]:i[1] + int(1.5 * i[3]), i[0]:i[0] + int(1.5 * i[2])]
    cv2.imwrite(r'''image%s.png''' % c, crop_img)
    # Return Shape Guess
    label_image.main(r'''image%s.png''' % c,
                     r'''output_labels.txt''',
                     r'''retrained_graph.pb''')
    # Return Letter Guess
    label_image.main(r'''image%s.png''' % c,
                     r'''letters_labels.txt''',
                     r'''letters_graph.pb''')
    c += 1
