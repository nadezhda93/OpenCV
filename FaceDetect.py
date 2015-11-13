import cv2
import numpy as np
import sys

cascPath = sys.argv[1] #file name supplied in terminal
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

#define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'FFV1')
out = cv2.VideoWriter('faceTracking.avi', fourcc, 30.0,(640, 480), True)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    #write out the frame
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
# stop capturing video
out.release()
cv2.destroyAllWindows()