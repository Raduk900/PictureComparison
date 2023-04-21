from rembg import remove
import cv2
import numpy as np
import os
from PIL import Image    

img = cv2.imread('C:/Users/radtitk/Desktop/bakalaur/PictureComparison/Pictures/image3.jpg')
# img = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(img)
rgb_im = image_pil.convert('RGB')
output_path = 'output3.png'
output = remove(rgb_im)
output.save(output_path)




