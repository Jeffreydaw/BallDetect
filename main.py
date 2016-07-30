# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:39:20 2016

@author: alex
"""

import InputOutput
import ImageProcessing
import cv2

fx = 843
obj_width = 0.305 #meters 

def get_distance_to_camera(width):
    return (obj_width * fx) / width
    
if __name__ == '__main__':
    #img = InputOutput.get_image('Circles.png')
    #InputOutput.display_image(img,'Sample Image')

    image = InputOutput.get_image('PH2RedBalls.jpg')
    #image = InputOutput.get_image('OnWater.jpg')
    InputOutput.display_image(image,"Starting Image")

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV for thresholding
    image_hsv = cv2.blur(image_hsv, (9,9)) # blur to reduce noise

    thresh = ImageProcessing.thresholdRed(image_hsv)
    InputOutput.display_image(thresh,"Thresholded")
    thresh = ImageProcessing.removeNoise(thresh)    
    
    circles = ImageProcessing.houghTransform(thresh)       
"""
if __name__ == '__main__':
    #img = InputOutput.get_image('Circles.png')
    #InputOutput.display_image(img,'Sample Image')

    image = InputOutput.get_image('webcamVid1.jpg')
    InputOutput.display_imagen(image,"Starting Image")

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV for thresholding
    image_hsv = cv2.blur(image_hsv, (9,9)) # blur to reduce noise

    thresh = ImageProcessing.thresholdRed(image_hsv)
    InputOutput.display_image(thresh,"Thresholded")
    #thresh = ImageProcessing.removeNoise(thresh)    
    
    circles = ImageProcessing.houghTransform(thresh)
    """
