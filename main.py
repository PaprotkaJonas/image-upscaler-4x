import cv2
import os

def upscale():
    input_folder = "input"
    output_folder = "output"
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            img = cv2.imread(file_path)
            width = img.shape[1]
            height = img.shape[0]
            new_width = width * 4
            new_height = height * 4
            new_img = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_LINEAR)
            save_path = os.path.join(output_folder, file)
            cv2.imwrite(save_path, new_img)
upscale()
