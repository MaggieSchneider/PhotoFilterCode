# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:33:30 2021
Photo Filter Code
@author:Maggie Schneider S2112038
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path

#color library
color_list = [[0,0,255], [0,255,255], [255,0,0], [0,255,0], [150,200,0], [200,0,200], [50,100,25], [255,255,255],[0,0,0],[180,105,255]]
#color_list[0]= true red
#color_list[1]= true yellow
#color_list[2]= true blue
#color_list[3]= true green
#color_list[4]= dark green
#color_list[5]= purple
#color_list[6]= teal
#color_list[7]= white
#color_list[8]= black
#color_list[9]= hot pink

def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Value is too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    else:
        return current_pos



#making sure your file can run
print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#make grayscale
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#make windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Color_1 Parts of Image')
#cv2.namedWindow('Color_2 Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders')

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#size the paper correctly
color_1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_3_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_4_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_5_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_6_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color_7_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)

#assign color to paper, put color in from library
color_1_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[0]]
color_2_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[1]]
color_3_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[2]]
color_4_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[3]]
color_5_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[4]]
color_6_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[5]]
color_7_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[6]]

#make trackbars
cv2.createTrackbar('Grayscale', 'Sliders', 50, 255, lambda x:None)
cv2.createTrackbar('Grayscale2', 'Sliders', 75, 255, lambda x:None)
cv2.createTrackbar('Grayscale3', 'Sliders', 100, 255, lambda x:None)
cv2.createTrackbar('Grayscale4', 'Sliders', 125, 255, lambda x:None)
cv2.createTrackbar('Grayscale5', 'Sliders', 150, 255, lambda x:None)
cv2.createTrackbar('Grayscale6', 'Sliders', 200, 255, lambda x:None)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
  
keypressed = 1

#assign colors to sliders and change how far sliders can move
while(keypressed != 27 and keypressed != ord('s')):
    grayscale_break = trackPosition('Grayscale', 'Sliders', 50)
    grayscale_break2 = trackPosition('Grayscale2', 'Sliders', 75)
    grayscale_break3 = trackPosition('Grayscale3', 'Sliders', 100)
    grayscale_break4 = trackPosition('Grayscale4', 'Sliders', 125)
    grayscale_break5 = trackPosition('Grayscale5', 'Sliders', 150)
    grayscale_break6 = trackPosition('Grayscale6', 'Sliders', 200)
    
    min_grayscale_for_color_1 = [0,0,0]
    max_grayscale_for_color_1 = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_color_2 = [grayscale_break+1,grayscale_break+1, 
                                grayscale_break+1]
    max_grayscale_for_color_2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_color_3 = [grayscale_break2+1,grayscale_break2+1,grayscale_break2+1]
    max_grayscale_for_color_3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_color_4 = [grayscale_break3+1,grayscale_break3+1,grayscale_break3+1]
    max_grayscale_for_color_4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_color_5 = [grayscale_break4+1,grayscale_break4+1,grayscale_break4+1]
    max_grayscale_for_color_5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_color_6 = [grayscale_break5+1,grayscale_break5+1,grayscale_break5+1]
    max_grayscale_for_color_6 = [grayscale_break6,grayscale_break6,grayscale_break6]
    min_grayscale_for_color_7 = [grayscale_break6+1,grayscale_break6+1,grayscale_break6+1]
    max_grayscale_for_color_7 = [255,255,255]
    
    min_grayscale_for_color_1 = numpy.array(min_grayscale_for_color_1, dtype = "uint8")
    max_grayscale_for_color_1 = numpy.array(max_grayscale_for_color_1, dtype = "uint8")
    min_grayscale_for_color_2 = numpy.array(min_grayscale_for_color_2,
                                           dtype = "uint8")
    max_grayscale_for_color_2 = numpy.array(max_grayscale_for_color_2,
                                           dtype = "uint8")
    min_grayscale_for_color_3 = numpy.array(min_grayscale_for_color_3,
                                           dtype = "uint8")
    max_grayscale_for_color_3 = numpy.array(max_grayscale_for_color_3,
                                           dtype = "uint8")
    min_grayscale_for_color_4 = numpy.array(min_grayscale_for_color_4,
                                           dtype = "uint8")
    max_grayscale_for_color_4 = numpy.array(max_grayscale_for_color_4,
                                           dtype = "uint8")
    min_grayscale_for_color_5 = numpy.array(min_grayscale_for_color_5,
                                           dtype = "uint8")
    max_grayscale_for_color_5 = numpy.array(max_grayscale_for_color_5,
                                           dtype = "uint8")
    min_grayscale_for_color_6 = numpy.array(min_grayscale_for_color_6,
                                           dtype = "uint8")
    max_grayscale_for_color_6 = numpy.array(max_grayscale_for_color_6,
                                           dtype = "uint8")
    min_grayscale_for_color_7 = numpy.array(min_grayscale_for_color_7,
                                           dtype = "uint8")
    max_grayscale_for_color_7 = numpy.array(max_grayscale_for_color_7,
                                           dtype = "uint8")
    
    block_all_but_the_color_1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color_1,
                                              max_grayscale_for_color_1)
    block_all_but_the_color_2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_2,
                                                 max_grayscale_for_color_2)
    block_all_but_the_color_3_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_3,
                                                 max_grayscale_for_color_3)
    block_all_but_the_color_4_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_4,
                                                 max_grayscale_for_color_4)
    block_all_but_the_color_5_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_5,
                                                 max_grayscale_for_color_5)
    block_all_but_the_color_6_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_6,
                                                 max_grayscale_for_color_6)
    block_all_but_the_color_7_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color_7,
                                                 max_grayscale_for_color_7)
    
    color_1_parts_of_image = cv2.bitwise_or(color_1_paper, color_1_paper,
                                        mask = block_all_but_the_color_1_parts)
    color_2_parts_of_image = cv2.bitwise_or(color_2_paper, color_2_paper,
                                           mask = block_all_but_the_color_2_parts)
    color_3_parts_of_image = cv2.bitwise_or(color_3_paper, color_3_paper,
                                           mask = block_all_but_the_color_3_parts)
    color_4_parts_of_image = cv2.bitwise_or(color_4_paper, color_4_paper,
                                           mask = block_all_but_the_color_4_parts)
    color_5_parts_of_image = cv2.bitwise_or(color_5_paper, color_5_paper,
                                           mask = block_all_but_the_color_5_parts)
    color_6_parts_of_image = cv2.bitwise_or(color_6_paper, color_6_paper,
                                           mask = block_all_but_the_color_6_parts)
    color_7_parts_of_image = cv2.bitwise_or(color_7_paper, color_7_paper,
                                           mask = block_all_but_the_color_7_parts)
    
    #add the colors into the customized image 
    customized_image = cv2.bitwise_or(color_1_parts_of_image, color_2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_7_parts_of_image)
    
    #cv2.imshow('Color_1 Parts of Image',Color_1_parts_of_image)
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'):
    new_file = input ('Name file now, include .jpg at end:')
    #cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite(new_file,customized_image)
    cv2.destroyAllWindows()
