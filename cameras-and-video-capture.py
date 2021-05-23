import cv2
import numpy as np

#
''' If you've multiple cameras then cv2.VideoCapture(0) will access one camera,
    cv2.VideoCapture(1) will access the other one and so on. If you've only one 
    camera then use 0 in cv2.VideoCapture(0).

    You can also use video files by passing the filename as a parameter in 
    the VideoCapture method of cv2 like cv2.VideoCapture('filename.mp4') '''


# Single frame
def display_simple_frame():
    capture = cv2.VideoCapture(0)

    while True:
        # _return value will tell if this capture worked properly
        _return, frame = capture.read()
        cv2.imshow('Frame', frame)

        # Checking if in 1 millisec the user pressed 'q', if yes then quit
        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    capture.destroyAllWindows()


# 4 separate frames
def display_multiple_frames():
    capture = cv2.VideoCapture(0)

    while True:
        _return, frame = capture.read()

        # This frame is what will be displayed 4 times
        img = np.zeros(frame.shape, np.uint8)

        # So to display the img 4 times in the frame we've to decrease the size
        # of the img and since we're decreasing the height and widht by halft so
        # we'll have space for 4 frames
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Getting width and height of the frame
        # capture has multiple properties and get their values use get method with the
        # property number. For width and height the property number is 3 and 4 respectively
        width = int(capture.get(3))
        height = int(capture.get(4))

        # Pasting the frame into 4 sections of frame
        img[:height // 2, :width // 2] = smaller_frame  # top left
        img[height // 2:, :width // 2] = smaller_frame  # bottom left
        img[:height // 2, width // 2:] = smaller_frame  # top right
        img[height // 2:, width // 2:] = smaller_frame  # bottom right

        cv2.imshow('Frame', img)

        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    capture.destroyAllWindows()


# display_multiple_frames()


# 4 separate frames with rotations
def display_multiple_frames_with_rotation():
    capture = cv2.VideoCapture(0)

    while True:
        _return, frame = capture.read()

        img = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        width = int(capture.get(3))
        height = int(capture.get(4))

        img[:height // 2, :width // 2] = cv2.rotate(
            smaller_frame,
            cv2.cv2.ROTATE_180,
        )
        img[height // 2:, :width // 2] = smaller_frame
        img[:height // 2, width // 2:] = cv2.rotate(
            smaller_frame,
            cv2.cv2.ROTATE_180,
        )
        img[height // 2:, width // 2:] = smaller_frame

        cv2.imshow('Frame', img)

        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    capture.destroyAllWindows()


display_multiple_frames_with_rotation()
