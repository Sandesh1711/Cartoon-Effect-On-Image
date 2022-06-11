# Importing library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# loading input image

def read_image(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("Image",img)
    return img

path = input("enter the image path:-")
result = read_image(path)
cv2.waitKey(0)
