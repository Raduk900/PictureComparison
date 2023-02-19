# Opens I as an array
# I = numpy.asarray(PIL.Image.open('test.jpg'))

# Converts to pil  image
# im = PIL.Image.fromarray(numpy.uint8(I))
import cv2
import numpy as np
from PIL import ImageFilter


def orb_sim(img1, img2):
    orb = cv2.ORB_create()

    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(desc_a, desc_b)

    similar_regions = [i for i in matches if i.distance < 50]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)


def import_grey_images():
    im_gray1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
    im_gray2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

    return im_gray1, im_gray2


def convert_to_black_white(img1, img2):
    (thresh, im_bw1) = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, im_bw2) = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    im_bw1 = cv2.threshold(img1, thresh, 255, cv2.THRESH_BINARY)[1]
    im_bw2 = cv2.threshold(img2, thresh, 255, cv2.THRESH_BINARY)[1]

    return im_bw1, im_bw2


def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blur_images(img1, img2):
    blur1 = cv2.blur(img1, (10, 10))
    blur2 = cv2.blur(img2, (10, 10))

    return blur1, blur2

def cut_main_object():
    image = cv2.imread('image1.jpg')

    # Convert the image to grayscale
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    mask = cv2.drawContours(np.zeros_like(image), [largest_contour], 0, (255, 255, 255), -1)
    cut_out = cv2.bitwise_and(image, mask)

    return cut_out

img1, img2 = import_grey_images()

bw1, bw2 = convert_to_black_white(img1, img2)

blur1, blur2 = blur_images(img1, img2)

orb_similarity = orb_sim(bw1, bw2)

print("Similarity using ORB is: ", orb_similarity)

image = cv2.imread("image1.jpg")
# blurimg = cv2.blur(image, (20, 20))

# cutted = cut_main_object()

show_image(img1)
