from random import randrange

import cv2

IMG_PATH = './assets/man-holding-camera.jpg'

img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
''' NOTE

    Rows     - Height
    Columns  - Width
    Depth    - Channels
'''


def display_img(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_info(img):
    # img is numpy.ndarray

    print(f'Shape: {img.shape}')  # ex: (4472, 6708, 3) - (h, w, c)

    print(f'Random row (height): {img[100]}')
    print(f'Random column (width): {img[100][0]}')

    print(f'Height (rows): {len(img)}')
    print(f'Wdith (columns): {len(img[100])}')
    print(f'Depth (channel): {len(img[100][0])}')


# img_info(img)


# Changing the colors in the img
def randomize_change(img):
    # Randomizing the color values in top (img_total_width X 500) - (w X h)
    # space in the img
    for row_idx in range(500):
        for col_idx in range(img.shape[1]):
            # Assigning random colors to the 3 channels
            img[row_idx][col_idx] = [
                randrange(255),
                randrange(255),
                randrange(255),
            ]

    display_img(img)


# randomize_change(img)


# Copying one part of img and pasting it in other part of an img
def copy_paste_img(img):
    # copying pixels from 1000:1499 (height - 499px) and 2500:4499 (width - 1999px)
    # this just copying a rectangular part from the img
    copy_part = img[1000:1500, 2500:4500]

    # pasting the copied part in the same img
    img[2100:2600, 3600:5600] = copy_part

    display_img(img)


copy_paste_img(img)
