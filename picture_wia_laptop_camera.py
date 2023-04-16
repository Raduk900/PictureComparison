import cv2
import os

def num_of_images():

    pictures_path = "C:/Users/radek/PycharmProjects/bakalaur/Python/PictureComparison/Pictures"
    extensions = [".jpg", ".jpeg", ".png"]

    images = 0

    for file_name in os.listdir(pictures_path):
        if os.path.splitext(file_name)[-1].lower() in extensions:
            images += 1

    return images

def capture_image():
    counter = num_of_images()

    imagePath = "C:/Users/radek/PycharmProjects/bakalaur/Python/PictureComparison/Pictures/image" + str(counter + 1)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Press 'p' to capture image", frame)
        key = cv2.waitKey(1)
        if key == ord('p'):
            cv2.imwrite(imagePath, frame)
            break
    cap.release()
    cv2.destroyAllWindows()

capture_image()