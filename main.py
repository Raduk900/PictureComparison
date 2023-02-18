# Opens I as an array
# I = numpy.asarray(PIL.Image.open('test.jpg'))

# Converts to pil  image
# im = PIL.Image.fromarray(numpy.uint8(I))




import cv2
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


im_gray1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
im_gray2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

blur_image = im_gray1.filter(ImageFilter.BLUR)

# (thresh, im_bw1) = cv2.threshold(im_gray1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# (thresh, im_bw2) = cv2.threshold(im_gray2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
# im_bw1 = cv2.threshold(im_gray1, thresh, 255, cv2.THRESH_BINARY)[1]
# im_bw2 = cv2.threshold(im_gray2, thresh, 255, cv2.THRESH_BINARY)[1]

orb_similarity = orb_sim(im_gray1, im_gray2)

cv2.imshow("image", blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Similarity using ORB is: ", orb_similarity)


