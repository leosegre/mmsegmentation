# Code to apply operations on all the images
# present in a folder one by one
# operations such as rotating, cropping,
from PIL import Image
from PIL import ImageFilter
import cv2
import os
import numpy as np


def main():
    # path of the folder containing the raw images
    inPath = "/home/leo/data/Frederick_seg/labels"

    num_pixels = 0
    for imagePath in os.listdir(inPath):
        if "mask" in imagePath:
            # imagePath contains name of the image
            inputPath = os.path.join(inPath, imagePath)

            # inputPath contains the full directory name
            img = cv2.imread(inputPath, cv2.IMREAD_GRAYSCALE)
            img = np.array(img)
            num_pixels += (img != 255).sum()

    num_pixels_in_img = 1024*1024
    print("num_pixels:", num_pixels)
    print("effective images:", num_pixels/num_pixels_in_img)



# Driver Function
if __name__ == '__main__':
    main()