import cv2
import os
import image_helper
    
def capture_with_screenshot():
    
    counter = image_helper.num_of_images()

    path = image_helper.relative_path()

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
