import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def all_greater(list1, list2):
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            return False
    return True

def one_greater(list1, list2):
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            return True
    return False

#mode=None: manual thresholding
#mode=and: manual thresholding with and
#mode=or: manual thresholding with or
def manual_threshold(image, threshold, mode=None):
    new_image = np.zeros(image.shape, dtype=int)
    if mode != None:
        if (mode.upper() == "AND"):
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    for k in range(image.shape[2]):
                        if all_greater(image[i][j], threshold):
                            new_image[i][j][k] = 255
                        else :
                            new_image[i][j][k] = 0

        elif mode.upper() == "OR":
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    for k in range(image.shape[2]):
                        if one_greater(image[i][j], threshold):
                            new_image[i][j][k] = 255
                        else :
                            new_image[i][j][k] = 0
    else:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(image.shape[2]):
                    if image[i][j][k] >= threshold[k]:
                        new_image[i][j][k] = 255
                    elif image[i][j][k] < threshold[k]:
                        new_image[i][j][k] = 0
                    else:
                        new_image[i][j][k] = image[i][j][k]
    return new_image

#execution:
#img = Image.open("assets/house.ppm").convert('RGB')
#img_array = np.asarray(img)
#img_threshold = manual_threshold(img_array, [155, 155, 155],mode="and")
#plt.imshow(img_threshold)
