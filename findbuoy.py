
# code bits copied from:
# http://stackoverflow.com/questions/30331944/finding-red-color-using-python-opencv
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html?highlight=houghcircles

import cv2

# load image
img = cv2.imread('redbuoy.jpg')

# convert to hue, saturation, value
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# find places in the image with a hue of less than 10 or more than 170
# because red is at both ends of the hue spectrum of hsv
# also make sure it's got at least a little saturation.

# lower mask (0-10)
lower_red = (0, 80, 80)
upper_red = (10, 255, 255)
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = (170, 80, 80)
upper_red = (180, 255, 255)
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join masks to make a binary image where red is white and nonred is black
redspace = mask0 + mask1

# find circles
circles = cv2.HoughCircles(redspace, cv2.cv.CV_HOUGH_GRADIENT, 3.5, 40, minRadius=150)

print circles

# draw circle
for circle in circles[0]:
    cv2.circle(redspace, (circle[0], circle[1]), circle[2], (0, 0, 0), 5)

# make a tiny window
cv2.namedWindow('output', 0)
cv2.resizeWindow('output', 500, 500)

# show output
cv2.imshow('output', redspace)

# stuff for letting windows show
cv2.waitKey(0)
cv2.destroyAllWindows()
