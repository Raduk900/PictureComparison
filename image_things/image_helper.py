import os
import cv2
import requests

def num_of_images():

    pictures_path = relative_path()
    extensions = [".jpg", ".jpeg", ".png"]

    images = 0

    for file_name in os.listdir(pictures_path):
        if os.path.splitext(file_name)[-1].lower() in extensions:
            images += 1

    return images

def relative_path():
    absolute_path = os.path.dirname(__file__)
    end_path = "Pictures"
    full_path = os.path.join(absolute_path, end_path).replace('\\', '/')
    
    return full_path

def take_last_gray_image():

    path = relative_path()
    max_index = num_of_images()
    picture_path = path + "/image" + str(max_index) + ".jpg"
    grey_image = cv2.imread(picture_path, cv2.IMREAD_GRAYSCALE)
    
    return grey_image

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
def download_image(url):
    
    print("it is url: ", url)
    
    filename = "image.jpg"

    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)
        
def delete_image(filename):

    if os.path.exists(filename):
        os.remove(filename)
        print("Image deleted successfully")
    else:
        print("Image does not exist")
