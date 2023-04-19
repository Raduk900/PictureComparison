import cv2
import os

def num_of_images():

    pictures_path = relative_path()
    extensions = [".jpg", ".jpeg", ".png"]

    images = 0

    for file_name in os.listdir(pictures_path):
        if os.path.splitext(file_name)[-1].lower() in extensions:
            images += 1

    return images
    
def capture_with_screenshot():
    
    counter = num_of_images()

    path = relative_path()

    imagePath = path + "/image" + str(counter + 1) + ".jpg"

    cap = cv2.VideoCapture(0)
    
    #full screen video
    # cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
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
    
def relative_path():
    absolute_path = os.path.dirname(__file__)
    end_path = "Pictures"
    full_path = os.path.join(absolute_path, end_path).replace('\\', '/')
    
    return full_path

capture_with_screenshot()