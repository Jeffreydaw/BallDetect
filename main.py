# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:39:20 2016

@author: alex
"""

import InputOutput
import ImageProcessing
import cv2
import math
import sys    

fx = 843
obj_width = 0.305 #meters

def get_distance_to_camera(width):
    return (obj_width * fx) / width

if __name__ == '__main__':
    #img = InputOutput.get_image('Circles.png')
    #InputOutput.display_ima ge(img,'Sample Image')

    #Stores a list of files along with the correct x,y,radius position of any balls
    #filename,((x,y,radius),(x,y,radius)...)
    
    correct_circles = (('OnWater1.jpg',((520,312,100),)),('OnDeck.jpg',((731,416,106),))
        ,('TwoBalls.jpg',((519,308,106),(1534,312,106))))
    circle_comparisons = []
    num_balls = 0
    for file_name,measur_circle in correct_circles:
        #Keep track of the number of balls measured
        num_balls+= len(measur_circle)   
        
        image = InputOutput.get_image(file_name)
        InputOutput.display_image(image,"Starting Image")

        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV for thresholding
        image_hsv = cv2.blur(image_hsv, (9,9)) # blur to reduce noise
 
        thresh = ImageProcessing.thresholdRed(image_hsv)
        InputOutput.display_image(thresh,"Thresholded")
        thresh = ImageProcessing.removeNoise(thresh)    
    
        #calc_circles = ImageProcessing.houghTransform(thresh)
        calc_circles = ImageProcessing.blob_circle_detection(thresh)
        if calc_circles == None:
            calc_circles = []
        #calc_circles = ImageProcessing.get_blob_centroid(image, thresh, 5)
         
        InputOutput.display_image_with_circles(image,"Result!",calc_circles)
        
        #evalueateSuccess by comparing the circle position with the most similar
        #red ball's measured circle.
        
        #Print basic file facts
        print ("")
        print ("file: " + file_name)
        print ("# of Balls in image: " + str(len(measur_circle)))
        print ("# of Balls detected: " + str(len(calc_circles)))  
        
        #Figure out which 
        for calc_x,calc_y,calc_radis in calc_circles:
            #search for most similar circle
            #setup inital values for first run
            closest_x,closest_y,closest_radius = -10000,-10000,-100000
            closest_distance = 1000000
            for measur_x,measur_y,measur_radius in measur_circle:
                distanceToCenter = math.sqrt(math.pow((calc_x-measur_x),2)+math.pow((calc_y-measur_y),2))
                if(closest_distance>distanceToCenter):
                    closest_x = measur_x
                    closest_y = measur_y
                    closest_radius = measur_radius
                    closest_distance = distanceToCenter
            
                        
            circle_comparisons.append((closest_x, closest_y, closest_radius
                , calc_x , calc_y, calc_radis))
            print (closest_x, closest_y, closest_radius
                , "-> " , calc_x , calc_y, calc_radis)
    
    #Print Summary Statistics
    num_balls_detected = len(circle_comparisons)  
    
    if(num_balls_detected == 0):
        print "No balls detected"
        sys.exit()
    
    #Get average error
    total_xy_error = 0
    total_radius_error = 0
    for measured_x, measured_y, measured_radius, calc_x, calc_y, calc_radius in circle_comparisons:
        total_xy_error = total_xy_error + math.sqrt(math.pow((calc_x-measured_x),2)+math.pow((calc_y-measured_y),2))
        total_radius_error = total_radius_error + abs(measured_radius-calc_radius)
    
    avg_xy_error = total_xy_error/num_balls_detected
    avg_radius_error = total_radius_error/num_balls_detected
    
    #Search for undetected circles and circles detected twice
    num_unique_detections = 0
    
    for i in range(num_balls_detected):
        unique = True
        for j in  range(num_balls_detected-i-1):
            x_equal = circle_comparisons[i][0]==circle_comparisons[i+j+1][0]
            y_equal = circle_comparisons[i][1]==circle_comparisons[i+j+1][1]
            radius_equal =  circle_comparisons[i][2]==circle_comparisons[i+j+1][2]
            if(x_equal and y_equal and radius_equal):
                unique = False
        if(unique== True):
            num_unique_detections+=1
                
    print "\n--- Summary Statistics ---"
    print "Average XY error: " + str(avg_xy_error)
    print "Average radius error: " + str(avg_radius_error)
    print str(num_unique_detections) + " of " + str(num_balls) + " balls detected"
    print str(num_balls_detected-num_unique_detections) + " of " + str(num_balls_detected) + " balls detections were duplicate detections"
