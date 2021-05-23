import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    _return, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Displaying only the blue color objects
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Masking the portion which is not in lower OR upper blue
    # the mask return by inRange method tells us which portion to
    # keep i.e. the portion where colours lies between upper and
    # lower blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # We'll use the mask and apply it to our img and keep the part
    # which lies in the upper and lower blue of the mask. So we'll
    # compare pixel by pixel and see if the pixel is blue, if yes
    # then keep it else turn it to black
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # https://stackoverflow.com/a/51905557 this post will help to understand why
    # frame is used 2 time.
    # quick answer => dst(I) = sur1(I) ^sur2(I), if mask(I) != 0,

    cv2.imshow('Frame', result)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
capture.destroyAllWindows()

# Converting 1 pixel to HSV, but be carefull since cvtColor method needs
# an image, so while passing 1 pixel pass it in the format of (rows, columns, channels)
bgr_color = np.array([[[255, 0, 0]]])
img = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
# img[0][0] # you'll get the one pixel
