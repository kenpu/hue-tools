import cv2
import time

cap = cv2.VideoCapture(1)

try: 
    while True:
        ret, im = cap.read()
        im = cv2.flip(im, 0)
        im = cv2.flip(im, 1)
        cv2.imshow('window', im)
        key = cv2.waitKey(1) & 0xff

        if key == ord('q'):
            break
except Exception as e:
    print "Caught:", e


cap.release()
cv2.destroyAllWindows()
