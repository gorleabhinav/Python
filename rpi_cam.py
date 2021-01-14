# capture and display an image in a window
import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        print("Unable to read frame")
        break
    cv2.imshow("window", frame)
    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
