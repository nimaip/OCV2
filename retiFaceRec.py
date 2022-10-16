import cv2
from simple_facerec import SimpleFacerec
import time

def takePic(c, counter):
    print(cv2.imwrite('intruders/pic' + str(counter) + '.jpg', c))
    counter += 1
    time.sleep(0.01)


sfr = SimpleFacerec()
sfr.load_encoding_images("fam/")

cap = cv2.VideoCapture(1)

counter = 1
lastX = lastY = 0
x1 = y1 = 0
while True:
    ret, frame = cap.read()

    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)

    if not(x1 == lastX and y1 == lastY):
        print("taking pic")
        takePic(frame, counter)
        counter+=1

    lastX = x1
    lastY = y1


cap.release()
cv2.destroyAllWindows