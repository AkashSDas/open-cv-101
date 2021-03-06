import cv2
import numpy as np

img = cv2.imread('./assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey_img, 200, 0.01, 10)
# print(corners)
# Converting the floating point values into int since we want to draw
# circles to for the place where the algorithm has detected as corner
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
