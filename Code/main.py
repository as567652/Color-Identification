# import important modules
import cv2 as cv
import numpy as np

# defining path to image file
path_to_img = 'Code/test_images/Cars/blue_car.jpeg'

# reading image from specified path
img = cv.imread(path_to_img)

# dispalying image based on image size
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


# variables for pixel counts
pixel_dic = {'Red' : 0, 'Green' : 0, 'Blue' : 0, 'White' : 0}


# function to count pixel frequency
def pixel_count(color, hsv_img_mask):
    for i in range(0, len(hsv_img_mask)):
        for j in range(0, len(hsv_img_mask[0])):
            if (hsv_img_mask[i][j] != 0):
                pixel_dic[color] += 1


# function to apply mask
def applying_mask(h, color, display):
    if (color == 'White'):
        lower = np.array([0, 0, 100])
        upper = np.array([20, 0, 255])
    else:
        lower = np.array([h - 20, 100, 100])
        upper = np.array([h + 20, 255, 255])
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    if (display):
        show_img(mask, color + ' Mask')

    # cropping image
    centre = (img.shape[1] // 2, img.shape[0] // 2)
    crop_l = min(img.shape[1] // 4, img.shape[0] // 4)
    c_img = img[centre[1] - crop_l : centre[1] + crop_l, centre[0] - crop_l : centre[0] + crop_l]
    c_hsv = cv.cvtColor(c_img, cv.COLOR_BGR2HSV)
    c_mask = cv.inRange(c_hsv, lower, upper)
    pixel_count(color, c_mask)


# Applying Different Masks and Showing Results
applying_mask(R_HSV[0][0][0], 'Red', True)
applying_mask(G_HSV[0][0][0], 'Green', True)
applying_mask(B_HSV[0][0][0], 'Blue', True)
applying_mask(W_HSV[0][0][0], 'White', True)


# sorting dictionary
pixel_dic = dict(sorted(pixel_dic.items(),key= lambda x:x[1], reverse = True))
print()
print(f'Color Of Given Image Is :- {list(pixel_dic.keys())[0]}')
print()