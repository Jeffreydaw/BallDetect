# -*- coding: utf-8 -*-

import cv2
import numpy as np
import InputOutput

#fx = 517 * 0.5 # focal length is calculated for 320x240
fx = 843
obj_width = 0.305 #meters

def houghTransform(image):
    #Apply the Hough Transform to find the circles
    circles = cv2.HoughCircles(image,cv2.cv.CV_HOUGH_GRADIENT,3 , 10) #2.3 is tp be screwed 2.5 is good
    
    #/// Apply the Hough Transform to find the circles
    if (circles is None):
        print "Hough transform called but no circles found."
        output = image.copy()
        InputOutput.display_image(np.hstack([image, output]),"houghTransform")
        return circles
    else:
        #circleList= []
        circles = np.round(circles[0, :]).astype("int")

        output = image.copy()
        # loop over the (x, y) coordinates and radius of the circles
       
        Sum_x=0
        Sum_y=0
        Sum_r=0

        count =0 
        for (x, y, r) in circles:
            #get aravage circle
            count = count+1            
            Sum_x= Sum_x +x #((ax*count)+x)/(count+1)
            Sum_y= Sum_y +y #((ay*count)+y)/(count+1)
            Sum_r= Sum_r + r #((ar*count)+r)/(count+1)
            #avaragedCircle=
            
            #circleList.append[circles]
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            
            cv2.circle(output, (x, y), r, (120, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            
        ax = Sum_x/count
        ay = Sum_y/count
        ar = Sum_r/count
        cv2.circle(output, (ax, ay), ar, (239, 239, 239), 4)
        cv2.rectangle(output, (ax -5, ay -5), (ax+ 5, ay+5), (239, 239, 239), -1)
        # show the output image
        InputOutput.display_image(np.hstack([image, output]),"houghTransform")
        return ((ax,ay,ar),)

#Convert the image from a color image to a thresholded image
def thresholdRed(image):
    #minGBR = (25, 14, 50)#(0,26,100) # 0,50,120
    #maxGBR = (130, 110, 255)#(15,243,255) #15, 200, 255
   # minGBR = ( 42, 50, 14)
   # maxGBR = ( 255,190, 110)
    
   # minGBR = np.array([0, 50, 60])#(0,26,100) # 0,50,120
   # maxGBR = (15, 200, 255)
   # minGBR= (0, 0, 0)#(0,26,100) # 0,50,120
    #maxGBR= (176, 255, 255)
    #minGBR= (0, 0, 0)
    #maxGBR= (176, 255, 255)
    lowerRedHSV = (0, 80, 90)
    upperRedHSV= (15, 255, 255)
    mask2 =cv2.inRange(image, lowerRedHSV, upperRedHSV)
    
    lower_red = (170, 80, 90)
    upper_red = (180, 255, 255)
    mask1 = cv2.inRange(image, lower_red, upper_red)
    totalMask = mask1 + mask2
    """
    lowerRedHSV = (0, 80, 80)
    upperRedHSV= (20, 255, 255)
    mask1 =cv2.inRange(image, lowerRedHSV, upperRedHSV)
    
    lower_red = (170, 80, 80)
    upper_red = (180, 255, 255)
    mask2 = cv2.inRange(image, lower_red, upper_red)"""

    totalMask = mask1 + mask2
    return totalMask
    
#Segments the image into blobs as seen from above
#image must be thresholded first
def getBlobs(image):
    shape = image.shape
    width = shape[0]
    height = shape[1]
    j_positions = [None]* width #stores all the locations of the tops of the objects
    
    #finds the first white or each x position when searching downwards
    for i in range(width):
        j = 0
        while(image[i,j] == 0):
            j+=1
            if(j >= height):
                break
        j_positions[i] = j
        print (i,j)
    
    #This is a list of found objects
    objects = []
    
    #tracking variables
    i = 0 #keeps track of scanning x position
    highest_pos = (0,height) # keeps track of x,y of the highest point of the object being considered
    start_x = 0 # the initial x position of the object
    is_looking_at_object = False #did the last col contain a white pixel
    
    while(i<width):
        if(j_positions[i]==height):
            if(is_looking_at_object == True):
                is_looking_at_object = False
                #add object information to list of found objects
                objects.append((start_x,i,highest_pos))
            #reset tracking variables to default positions the object is over
            highest_pos = (0,height)
            is_looking_at_object = False
            
        else:
            if(is_looking_at_object == False):
                start_x = i
                highest_pos = (i,j_positions[i])
                is_looking_at_object = True
            elif(highest_pos[1]>j_positions[i]):
                highest_pos = (i,j_positions[i])
        i+=1
    print objects
    return objects
    
def blob_circle_detection(image):
    blobs=getBlobs(image)
    circles = []
    for start_x,end_x,highest_pos in blobs:
        x = (end_x+start_x)/2
        radius = (end_x-start_x)/2
        circle = (int(x),highest_pos[1],int(radius))
        circles.append(circle)
    return circles
    
def removeReflection(image):
    #get the first highest white pixel's y position for each x
    32
    
#Removes any red noise picked up in image
def removeNoise(image):
	kernel = np.ones((9,9),np.uint8)
	# opening
	image = cv2.erode(image,kernel,iterations = 2)
	image = cv2.dilate(image,kernel,iterations = 2)
	
	# closing
	image = cv2.dilate(image,kernel,iterations =2)
	image = cv2.erode(image,kernel,iterations = 2)
	"""image = cv2.dilate(image,kernel,iterations =15)
	image = cv2.erode(image,kernel,iterations = 2)
	image = cv2.dilate(image,kernel,iterations =15)
	image = cv2.erode(image,kernel,iterations = 2)
	image = cv2.dilate(image,kernel,iterations =15)
	image = cv2.erode(image,kernel,iterations = 2)"""      
	return image

def get_blob_centroid(img, img_hsv, threshold=200):
    # Generate histogram for subregions of thresholded HSV image
    # Areas of interest are regions with white pixel count above a threshold
    thresh = img_hsv
    #thresh = thresholdRed(img_hsv)
    #InputOutput.display_image(thresh,"Thresholded")
    #thresh = removeNoise(thresh)
    
    aoi = []
    for i,j in np.ndindex((16,12)):
        roi = thresh[j*40:j*40+40,i*40:i*40+40]
        hist = cv2.calcHist([roi], [0], None, [1], [0,255])
        white_count = 1600 - int(hist[0][0])
        
        if white_count > threshold:
            aoi.append( (i,j, white_count) )

    # Naive grouping
    # Split image in half
    blobs = [[], []]
    for area in aoi:
        if area[0] <= 8:
            blobs[0].append(area)
        else:
            blobs[1].append(area)
            
    """blobs = []
    blobs.append(aoi)

    aoi2 = []
    for a1 in blobs[0]:
        i1 = a1[0]
        j1 = a1[1]
        
        diff_count = 0
        for a2 in blobs[0]:
            if (np.abs(a2[0] - i1) > 1) or (np.abs(a2[1] - j1) > 1):
                diff_count += 1

        if diff_count > len(blobs[0])/4:
            aoi2.append(a1)
            blobs[0].remove(a1)

    if len(aoi2) is not 0:
        print aoi2
        blobs.append(aoi2)"""
            
    points = []
    for blob in blobs:        
        # Find min and max AOI index in x and y axis
        minx = 16
        maxx = 0
        miny = 12
        maxy = 0
        for area in blob:
            if area[0] < minx:
                minx = area[0]
            if area[0] > maxx:
                maxx = area[0]

            if area[1] < miny:
                miny = area[1]
            if area[1] > maxy:
                maxy = area[1]

        # Center pixel of min/max AOI's
        minx_p = minx * 40 + 20
        maxx_p = maxx * 40 + 20
        miny_p = miny * 40 + 20
        maxy_p = maxy * 40 + 2

        # Centroid of AOI's
        centre_x = ((maxx_p - minx_p) / 2) + minx_p
        centre_y = ((maxy_p - miny_p) / 2) + miny_p

        # Radius of blob
        radius = 0
        rx = (maxx_p - minx_p) / 2
        ry = (maxy_p - miny_p) / 2
        if rx > ry:
            radius = rx
        else:
            radius = ry
        
        if radius >= 0:
            cv2.circle(img, (centre_x,centre_y), radius, (255,0,0), 2)
            cv2.imshow('out',img)
            cv2.waitKey(0)
        else:
            InputOutput.printWarning("Circle has a zero radius")

        points.append( (centre_x,centre_y,radius) )
        

    return points