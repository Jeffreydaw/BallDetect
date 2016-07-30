# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:35:49 2016

@author: alex
"""

import cv2
import numpy as np

display_images = True
supress_warnings = False

#For test purposes
def display_image(img,title):
    if display_images:
        cv2.imshow(title,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def get_image(fileName):
    image = cv2.imread("images/" + fileName,cv2.IMREAD_COLOR)
    
    if image is None:
        print "Failed to print image located at: " + "images/" + fileName
        return image
    else:
        height, width, channels = image.shape
        print height, width, channels
        return image
        
def printWarning(warning):
    if not supress_warnings:
        print warning