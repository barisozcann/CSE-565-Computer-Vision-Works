import cv2 as cv
import numpy as np


SourceImageCoordinates = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Creating Empty Array for Corner Coordinates 4x3

SourceImageCoordinates=np.array(SourceImageCoordinates)

ReferenceImageCoordinates = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #Creating Empty Array for Corner Coordinates 4x3
ReferenceImageCoordinates=np.array(ReferenceImageCoordinates)


color=(0,0,255) #Red Color

first_counter = 0

def marker1(event, x, y, flags, param):
    global first_counter
    
    if event == cv.EVENT_LBUTTONDOWN and first_counter != 4:
        SourceImageCoordinates[first_counter] = x, y, 1 #homogenous Coordinates
        
        cv.circle(img=source_image, center=(x, y), radius=7, color=color) #Special Pointer Function of OpenCV Library
        
        first_counter += 1 #Incrementing Counter
        cv.imshow('Source image', source_image)
        print('(',x,',',y,')')

second_counter = 0
def marker2(event, x, y, flags, param):
    global second_counter
    
    if event == cv.EVENT_LBUTTONDOWN and second_counter != 4:
        ReferenceImageCoordinates[second_counter] = x, y, 1 #homogenous Coordinates
        
        cv.circle(img=reference_image, center=(x, y), radius=7, color=color) #Special Pointer Function of OpenCV Library
        
        second_counter += 1 #Incrementing Counter
        cv.imshow('Reference image', reference_image)
        print('(',x,',',y,')')


source_image = cv.imread('Image5.png') #Source Image

reference_image = cv.imread('soccer_field.jpg') #Reference Image




cv.imshow('Source image', source_image)
cv.setMouseCallback('Source image', marker1)



cv.imshow('Reference image', reference_image)
cv.setMouseCallback('Reference image', marker2)

cv.waitKey(0)



matrix, mask = cv.findHomography(SourceImageCoordinates, ReferenceImageCoordinates,cv.RANSAC) #RANSAC means Random Sample Consensus

result_image = cv.warpPerspective(source_image, matrix, (len(reference_image[0]), len(reference_image))) #Result Image


cv.imshow("Result Image", result_image)

key = cv.waitKey(0)
