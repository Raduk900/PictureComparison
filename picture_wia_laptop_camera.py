import cv2
import os
import image_helper
import time
import find_similarity
import server.client as client
    
def capture_with_screenshot():
    
    counter = image_helper.num_of_images()

    path = image_helper.relative_path()

    imagePath = path + "/image" + str(counter + 1) + ".jpg"

    cap = cv2.VideoCapture(0)
    
    #full screen video
    #cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    if not cap.isOpened():
        print("Error opening camera")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame")
            break

        cv2.imshow("Press 'p' to take photo, press 'q' to quit the camera.", frame)
        
        key = cv2.waitKey(1)

        if key == ord('p'):
            # Take a screenshot and save it to a file
            cv2.imwrite(imagePath, frame)
            print("Screenshot taken!")
            
            
            time.sleep(2)
            
            last_image = image_helper.take_last_gray_image()
            image_for_compare = cv2.imread("C:/Users/radtitk/Desktop/bakalaur/PictureComparison/image11.jpg", cv2.IMREAD_GRAYSCALE)
            
            grey_similarity_result = find_similarity.grey_similarity(last_image,image_for_compare)
            blur_similarity_result = find_similarity.blur_similarity(last_image, image_for_compare)
            no_bg_similarity_result = find_similarity.no_bg_similarity(last_image, image_for_compare)
            
            print("Only gray: " + str(grey_similarity_result))
            print("Blure images: " + str(blur_similarity_result))
            print("Without bg: " + str(no_bg_similarity_result))
            
            score = grey_similarity_result + blur_similarity_result + no_bg_similarity_result
            
            if(score > int(1)):
                client.sending_data(int(101))
                print("Successful validation")
            else:
                print("Unsuccessful validation")


        # Check if the key pressed is 'q'
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
