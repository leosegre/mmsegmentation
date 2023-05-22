# Code to apply operations on all the images
# present in a folder one by one
# operations such as rotating, cropping,
from PIL import Image
from PIL import ImageFilter
import cv2
import os


def main():
    # path of the folder containing the raw images
    inPath = "/home/leo/data/Frederick/Group_10"

    # path of the folder that will contain the modified image
    outPath = "/home/leo/data/Frederick/Group_10"

    for imagePath in os.listdir(inPath):
        if "mask" in imagePath:
            # imagePath contains name of the image
            inputPath = os.path.join(inPath, imagePath)

            # inputPath contains the full directory name
            img = cv2.imread(inputPath, cv2.IMREAD_GRAYSCALE)

            fullOutPath = os.path.join(outPath, imagePath)
            # fullOutPath contains the path of the output
            # image that needs to be generated
            cv2.imwrite(fullOutPath, img-1)

            print(fullOutPath)


# Driver Function
if __name__ == '__main__':
    main()