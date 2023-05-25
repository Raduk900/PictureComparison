import numpy as np
from PIL import Image 

def convert_pil_to_cv2(image):
    
    converted = np.array(image) 
    
    return converted

def convert_cv2_to_pil(image):
    
    image_pil = Image.fromarray(image)
    
    return image_pil

def change_resolution(image):
    
    new_width = 640
    new_height = 480
    
    resized = image.resize((new_width, new_height))
    
    return resized