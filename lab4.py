import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


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
    
#execution:
#img = Image.open("assets/house.ppm").convert('RGB')
#img_array = np.asarray(img)
#img_threshold = manual_threshold(img_array, [155, 155, 155],mode="and")
#plt.imshow(img_threshold)

def erosion(image,size):
    img1= cv2.imread(image,0)
    m,n= img1.shape
    structuring_element= np.ones((size,size), dtype=np.uint8)
    constant= (size-1)//2
    img_erode= np.zeros((m,n), dtype=np.uint8)
    for i in range(constant, m-constant):
        for j in range(constant,n-constant):
            temp= img1[i-constant:i+constant+1, j-constant:j+constant+1]
            product= temp*structuring_element
            img_erode[i,j]= np.min(product)
    return img_erode


def dilatation(image):
    img1= cv2.imread(image,0)
    p,q= img1.shape
    img_dilate= np.zeros((p,q), dtype=np.uint8)
    structuring_element= np.array([[0,1,0], [1,1,1],[0,1,0]])
    constant1=1
    for i in range(constant1, p-constant1):
        for j in range(constant1,q-constant1):
            temp= img1[i-constant1:i+constant1+1, j-constant1:j+constant1+1]
            product= temp*structuring_element
            img_dilate[i,j]= np.max(product)

    return img_dilate

def fermeture(image,size):
    return erosion(dilatation(image), size)

def ouverture(image,size):
    return dilatation(erosion(image, size))
