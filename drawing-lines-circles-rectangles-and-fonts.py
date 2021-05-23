import cv2

#
''' Co-ordinate system of Open CV 

    Origin (0, 0) ----------------> x-axis
        |
        |
        |
        |
        |
        |
        |
        v
        y-axis
'''

caputer = cv2.VideoCapture(0)

while True:
    _, frame = caputer.read()

    width = int(caputer.get(3))
    height = int(caputer.get(4))

    # Colors
    blue_color = (255, 0, 0)
    green_color = (0, 255, 0)

    # Drawing a line
    thickness = 10
    img = cv2.line(frame, (0, 0), (width, height), blue_color, thickness)
    img = cv2.line(img, (width, 0), (0, height), green_color, thickness)

    # Drawing a rectangle
    top_pts = (100, 100)
    bottom_pts = (200, 200)
    thickness = 5
    img = cv2.rectangle(img, top_pts, bottom_pts, blue_color, thickness)

    # Drawing a circle
    center_pts = (300, 300)
    radius = 100
    # -1 means fill the cirlce, if we just want the outline then we can give it a
    # thickness instead of -1
    img = cv2.circle(img, center_pts, radius, blue_color, -1)

    # Draw a font
    # NOTE: For drawing text you need to follow the bottom-left hand co-ordinate where
    # the origin (0, 0) is in bottom-left hand instead of top-left hand
    font = cv2.FONT_HERSHEY_COMPLEX
    text = 'Open your CV'
    thickness = 5
    line_type = cv2.LINE_AA
    font_scale = 3
    img = cv2.putText(
        img, text, (200, height - 100), font, font_scale, green_color,
        thickness, line_type
    )

    cv2.imshow('Frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

caputer.release()
cv2.destroyAllWindows()
