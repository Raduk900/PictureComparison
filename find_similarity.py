import picture_wia_laptop_camera
import image_helper
import cv2
import image_preparation
import convertors
import orb_similarity

# picture_wia_laptop_camera.capture_with_screenshot()

last_image = image_helper.take_last_gray_image()
image_for_compare = cv2.imread("C:/Users/radtitk/Desktop/bakalaur/PictureComparison/image6.jpg", cv2.IMREAD_GRAYSCALE)

# def black_and_white_similartity(image1, image2):
    
#     black1, black2 = image_preparation.convert_to_black_white(image1, image2)
    
#     black1_pil = convertors.convert_cv2_to_pil(black1)
#     black2_pil = convertors.convert_cv2_to_pil(black2)
    
#     black1_no_bg = image_preparation.remove_background(black1_pil)
#     black2_no_bg = image_preparation.remove_background(black2_pil)
    
#     black1_cropped = image_preparation.crop_image(black1_no_bg)
#     black2_cropped = image_preparation.crop_image(black2_no_bg)
    
#     black1_resized = convertors.change_resolution(black1_cropped)
#     black2_resized = convertors.change_resolution(black2_cropped)
    
#     black1_cv = convertors.convert_pil_to_cv2(black1_resized)
#     black2_cv = convertors.convert_pil_to_cv2(black2_resized)
    
#     return orb_similarity.orb_sim(black1_cv, black2_cv)

def grey_similarity(image1, image2):
    
    return orb_similarity.orb_sim(image1, image2)

def blur_similarity(image1, image2):  

    last_pil_image = convertors.convert_cv2_to_pil(image1)
    pil_image = convertors.convert_cv2_to_pil(image2)

    last_no_bg = image_preparation.remove_background(last_pil_image)
    no_bg = image_preparation.remove_background(pil_image)

    cropped_last_pil = image_preparation.crop_image(last_no_bg)
    cropped_pil = image_preparation.crop_image(no_bg)

    resized_last_pil_image = convertors.change_resolution(cropped_last_pil)
    resized_pil_image = convertors.change_resolution(cropped_pil)

    last_cv_image = convertors.convert_pil_to_cv2(resized_last_pil_image)
    cv_image = convertors.convert_pil_to_cv2(resized_pil_image)

    blur1, blur2 = image_preparation.blur_images(last_cv_image, cv_image)
    
    # image_helper.show_image(blur1)
    # image_helper.show_image(blur2)
    
    return orb_similarity.orb_sim(blur1, blur2)

def no_bg_similarity(image1, image2):
    last_pil_image = convertors.convert_cv2_to_pil(image1)
    pil_image = convertors.convert_cv2_to_pil(image2)

    last_no_bg = image_preparation.remove_background(last_pil_image)
    no_bg = image_preparation.remove_background(pil_image)

    cropped_last_pil = image_preparation.crop_image(last_no_bg)
    cropped_pil = image_preparation.crop_image(no_bg)

    resized_last_pil_image = convertors.change_resolution(cropped_last_pil)
    resized_pil_image = convertors.change_resolution(cropped_pil)

    last_cv_image = convertors.convert_pil_to_cv2(resized_last_pil_image)
    cv_image = convertors.convert_pil_to_cv2(resized_pil_image)
    
    return orb_similarity.orb_sim(last_cv_image, cv_image)
    

def final_similarity():
    grey_similarity_result = grey_similarity(last_image,image_for_compare)
    blur_similarity_result = blur_similarity(last_image, image_for_compare)
    # black_and_white_similartity_result = black_and_white_similartity(last_image,image_for_compare)
    no_bg_similarity_result = no_bg_similarity(last_image, image_for_compare)
    
    print("Only gray: " + str(grey_similarity_result))
    print("Blure images: " + str(blur_similarity_result))
    # print("Black White: " + str(black_and_white_similartity_result))
    print("Without bg: " + str(no_bg_similarity_result))
        
    return grey_similarity_result + blur_similarity_result + no_bg_similarity_result

# score = final_similarity()

# print(score)