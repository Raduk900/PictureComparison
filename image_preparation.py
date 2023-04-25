import cv2
from rembg import remove
from PIL import Image

img1 = image_for_compare = cv2.imread("C:/Users/radtitk/Desktop/bakalaur/PictureComparison/image7.jpg", cv2.IMREAD_GRAYSCALE)
img2 = image_for_compare = cv2.imread("C:/Users/radtitk/Desktop/bakalaur/PictureComparison/image7.jpg", cv2.IMREAD_GRAYSCALE)

def convert_to_black_white(img1, img2):
    (thresh, im_bw1) = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, im_bw2) = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    im_bw1 = cv2.threshold(img1, thresh, 255, cv2.THRESH_BINARY)[1]
    im_bw2 = cv2.threshold(img2, thresh, 255, cv2.THRESH_BINARY)[1]

    return im_bw1, im_bw2

def remove_background(image):

    no_bg = remove(image)

    return no_bg

def crop_image(image):
    
    bbox = image.getbbox()
    
    cropped_image = image.crop(bbox)
    
    return cropped_image

def blur_images(img1, img2):
    
    blur1 = cv2.blur(img1, (10, 10))
    blur2 = cv2.blur(img2, (10, 10))
    
    return blur1, blur2

convert_to_black_white(img1,img2)