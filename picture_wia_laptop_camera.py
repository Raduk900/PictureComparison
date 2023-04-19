import cv2
import os

def num_of_images():

    pictures_path = "C:/Users/radtitk/Desktop/bakalaur/PictureComparison/Pictures"
    extensions = [".jpg", ".jpeg", ".png"]

    images = 0

    for file_name in os.listdir(pictures_path):
        if os.path.splitext(file_name)[-1].lower() in extensions:
            images += 1

    return images
    
def capture_with_screenshot():
    
    counter = num_of_images()

    imagePath = "C:/Users/radtitk/Desktop/bakalaur/PictureComparison/Pictures/image" + str(counter + 1) + ".jpg"

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error opening camera")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame")
            break

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)

        if key == ord('p'):
            # Take a screenshot and save it to a file
            cv2.imwrite(imagePath, frame)
            print("Screenshot taken!")

        # Check if the key pressed is 'q'
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

capture_with_screenshot()