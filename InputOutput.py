# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:35:49 2016

@author: alex
"""

import cv2
import cv2.cv as cv
import numpy as np

display_images = True
supress_warnings = False

max_width = 1500
max_height = 1200

#For test purposes
def display_image(img,title):
    if display_images:
        shape = img.shape
        if shape[0] > max_width or shape[1]>max_height:
            cv2.namedWindow(title,cv2.WINDOW_NORMAL)
        cv2.imshow(title,img)
        cv2.waitKey(0)
        cv2.destroyWindow(title)
        
def display_image_with_circles(img,title,circles):
   
    if not circles == None:
        if len(circles)>0:
            for x,y,radius in circles:
                 print x
                 print y
                 cv2.circle(img, (x,y), radius, (255,0,0), 2)        
            display_image(img,title)

def get_image(fileName):
    image = cv2.imread("images/" + fileName,cv2.IMREAD_COLOR)
    
    if image is None:
        print "Failed to print image located at: " + "images/" + fileName
        return image
    else:
        height, width, channels = image.shape
        return image


    
def printWarning(warning):
    if not supress_warnings:
        print warning