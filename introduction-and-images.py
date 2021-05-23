import cv2
import imutils

# Credit for the image
# Photo by Pursuit Retro on Unsplash

IMG_PATH = './assets/man-holding-camera.jpg'


def display_img(_path=IMG_PATH, view_img_mode=cv2.IMREAD_COLOR):
    img = cv2.imread(_path, view_img_mode)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# display_img()
# display_img(view_img_mode=cv2.IMREAD_GRAYSCALE)
# display_img(view_img_mode=0)
# display_img(view_img_mode=cv2.IMREAD_UNCHANGED)


def resize_img(_path=IMG_PATH):
    img = cv2.imread(_path, cv2.IMREAD_COLOR)

    # Resizing with absolute values
    img = cv2.resize(img, (600, 600))

    # Resizing with relative values of the img like half or quarter of the original
    # Here, halfing the img's height and width respectively
    # Here, fx and fy are the floating points that we want to multiply with the
    # number of pixels of height and with respectively
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # Doubling the img size
    img = cv2.resize(img, (0, 0), fx=2, fy=2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# resize_img()


def rotate_img(_path=IMG_PATH):
    img = cv2.imread(_path, cv2.IMREAD_COLOR)

    # This can rotate the img in following 3 ways only and not in custom angles
    # img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    # img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    # img = cv2.rotate(img, cv2.cv2.ROTATE_180)

    # Rotate img in custom angles
    img = imutils.rotate(img, 45)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# rotate_img()


def save_img(new_filename, _path=IMG_PATH):
    img = cv2.imread(_path, cv2.IMREAD_COLOR)
    img = imutils.rotate(img, 45)
    cv2.imwrite(new_filename, img)


save_img('./assets/man-holding-camera-at-45deg.jpg')
