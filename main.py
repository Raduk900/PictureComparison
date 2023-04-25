import picture_wia_laptop_camera
import image_helper
import cv2
import image_preparation
import convertors
import orb_similarity

# picture_wia_laptop_camera.capture_with_screenshot()

last_image = image_helper.take_last_gray_image()
image_for_compare = cv2.imread("C:/Users/radtitk/Desktop/bakalaur/PictureComparison/image6.jpg", cv2.IMREAD_GRAYSCALE)

black1, black2 = image_preparation.convert_to_black_white(last_image, image_for_compare)

# black1, black2 = image_preparation.convert_to_black_white(last_image, image_for_compare)

last_pil_image = convertors.convert_cv2_to_pil(last_image)
pil_image = convertors.convert_cv2_to_pil(image_for_compare)

black1_pil = convertors.convert_cv2_to_pil(black1)
black2_pil = convertors.convert_cv2_to_pil(black2)


last_no_bg = image_preparation.remove_background(last_pil_image)
no_bg = image_preparation.remove_background(pil_image)

black1_no_bg = image_preparation.remove_background(black1_pil)
black2_no_bg = image_preparation.remove_background(black2_pil)


cropped_last_pil = image_preparation.crop_image(last_no_bg)
cropped_pil = image_preparation.crop_image(no_bg)

black1_cropped = image_preparation.crop_image(black1_no_bg)
black2_cropped = image_preparation.crop_image(black2_no_bg)


resized_last_pil_image = convertors.change_resolution(cropped_last_pil)
resized_pil_image = convertors.change_resolution(cropped_pil)

black1_resized = convertors.change_resolution(black1_cropped)
black2_resized = convertors.change_resolution(black2_cropped)


last_cv_image = convertors.convert_pil_to_cv2(resized_last_pil_image)
cv_image = convertors.convert_pil_to_cv2(resized_pil_image)

blur1, blur2 = image_preparation.blur_images(last_cv_image, cv_image)

black1_cv = convertors.convert_pil_to_cv2(black1_resized)
black2_cv = convertors.convert_pil_to_cv2(black2_resized)

image_helper.show_image(cv_image)
image_helper.show_image(last_cv_image)



resized = convertors.change_resolution(pil_image)

print("Only gray: " + str(orb_similarity.orb_sim(last_image, image_for_compare)))
print("Blure images: " + str(orb_similarity.orb_sim(blur1, blur2)))
print("Black White: " + str(orb_similarity.orb_sim(black1_cv, black2_cv)))
print("Without bg: " + str(orb_similarity.orb_sim(cv_image, last_cv_image)))

# print("Image width: ", width)
# print("Image height: ", height)