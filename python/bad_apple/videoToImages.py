import cv2
import numpy
import os

videoName = "/bad_apple.mp4"
cap = cv2.VideoCapture(videoName[1:])
if not cap.isOpened(): print("Error opening file")
path = f"Y:/WINDOWS/__Programming__/Python Programs/opencv-python/{videoName[:-4]}"
count = 0

if not os.path.exists(path):
    os.makedirs(path)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imwrite(f"{path}/{count}.jpg", frame)
    count += 1

cap.release()
cv2.destroyAllWindows()
print("DONE")
