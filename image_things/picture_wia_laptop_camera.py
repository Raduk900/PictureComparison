import cv2
import os
import image_things.image_helper as image_helper
import time
import image_things.find_similarity as find_similarity
import server.client as client
import database.database_validations as database_validation
import tkinter as tk
    
def capture_with_screenshot(url):
    
    open = False
    
    counter = image_helper.num_of_images()

    path = image_helper.relative_path()

    imagePath = path + "/image" + str(counter + 1) + ".jpg"

    cap = cv2.VideoCapture(0)
    
    exit_camera = False
    
    print("THis is url in puicefasd: ", url)
    
    # #full screen video
    # cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    if not cap.isOpened():
        print("Error opening camera")
        return

    while not exit_camera:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame")
            break

        cv2.imshow("Press 'p' to take photo, press 'q' to quit the camera.", frame)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            exit_camera = True

        if key == ord('p'):
            # Take a screenshot and save it to a file
            cv2.imwrite(imagePath, frame)
            print("Screenshot taken!")
                 
            time.sleep(0.5)
            
            last_image = image_helper.take_last_gray_image()
            image_helper.download_image(url)
            image_for_compare = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
            
            
            
            # image_for_compare = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
            
            grey_similarity_result = find_similarity.grey_similarity(last_image,image_for_compare)
            # black = find_similarity.black_and_white_similartity(last_image, image_for_compare)
            blur_similarity_result = find_similarity.blur_similarity(last_image, image_for_compare)
            no_bg_similarity_result = find_similarity.no_bg_similarity(last_image, image_for_compare)
            
            # print("I am here")
            
            # print("Only gray: " + str(grey_similarity_result))
            # print("Blure images: " + str(blur_similarity_result))
            # print("Without bg: " + str(no_bg_similarity_result))
            # print("Black score: " + str(black))
            
            score = grey_similarity_result + blur_similarity_result + no_bg_similarity_result
            
            if(score > 0,1):
                client.sending_data(int(101))
                # print(score)
                print("Successful validation")
                time.sleep(10)
                client.sending_data(int(202))
                database_validation.add_to_user_take_item()
                break
            else:
                # print(score)
                print("Unsuccessful validation")
                tk.messagebox.showerror("Error", "Unsuccessful validation")
                
                


        # # Check if the key pressed is 'q'
        # if key == ord('q'):
        #     break

    cap.release()
    # cv2.destroyAllWindows()
