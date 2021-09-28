# import important modules
import cv2 as cv
import numpy as np

# defining path to image file
path_to_img = 'Code/test_images/Cars/red_car.jpeg'
# reading image from specified path
img = cv.imread(path_to_img)

def show_img(IMG, msg):
    if (IMG.shape[0] > 500 and IMG.shape[1] > 500):
        cv.imshow(msg, cv.resize(IMG, (500, 500), interpolation=cv.INTER_AREA))
    else:
        cv.imshow(msg, IMG)
    cv.waitKey(0)

# showing resized Original Image
show_img(img, 'Original Image')

# calculating HSV values for different colors 
R_HSV = cv.cvtColor(np.uint8([[[0, 0, 255]]]), cv.COLOR_BGR2HSV)
G_HSV = cv.cvtColor(np.uint8([[[0, 255, 0]]]), cv.COLOR_BGR2HSV)
B_HSV = cv.cvtColor(np.uint8([[[255, 0, 0]]]), cv.COLOR_BGR2HSV)
W_HSV = cv.cvtColor(np.uint8([[[255, 255, 255]]]), cv.COLOR_BGR2HSV)

# function to apply mask
def applying_mask(h, color):
    if (color == 'White'):
        lower = np.array([0, 0, 100])
        upper = np.array([20, 0, 255])
    else:
        lower = np.array([h - 20, 100, 100])
        upper = np.array([h + 20, 255, 255])
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    show_img(mask, color + 'Mask')

applying_mask(R_HSV[0][0][0], 'Red')
applying_mask(G_HSV[0][0][0], 'Green')
applying_mask(B_HSV[0][0][0], 'Blue')
applying_mask(W_HSV[0][0][0], 'White')