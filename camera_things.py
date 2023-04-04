import cv2

# specify the URL of the IP webcam
url = "http://192.168.137.1:8080/video"

# create a VideoCapture object with the IP webcam URL
cap = cv2.VideoCapture(url)

# read and display frames from the webcam
while True:
    ret, frame = cap.read()
    cv2.imshow('IP Webcam', frame)
    if cv2.waitKey(1) == 27:   # press the "Esc" key to exit
        break

cap.release()
cv2.destroyAllWindows()