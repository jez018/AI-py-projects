# -*- coding: utf-8 -*-
"""
New Pokemon Characters Generator
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import numpy as np
import os
import sklearn
from sklearn.preprocessing import MinMaxScaler
#from . import batch_list_images

def image_loader(dir_name):
    img_arr = []
    #Thhis piece of code loads the images from the file to memmory for easy usage
    for img_name in os.listdir(dir_name):
        #Load image
        img = Image.open(dir_name+'/'+img_name)
        #store in array
        img_arr.append(img)
    return img_arr

def black_and_white_converter():
    print('in b/w conv')
    #saves images to variable(also a memory loc)
    arr_img = image_loader('pokemon')
    bw_img_arr = []
    for img in arr_img:
        #load images to memmory
        img = img.convert('L')
        #img.show()
        bw_img_arr.append(img)
        
    #convert images to numpy for processing
    bw_img_arr = [np.asarray(img) for img in bw_img_arr]
    #rescale the images to 0 and 1
    bw_img_arr = [img/255.0 for img in bw_img_arr]
    #loop to rescale the data to -1 and 1 instead of 0 and 1
    n_img_arr = []
    for img in bw_img_arr:
        scl = MinMaxScaler(feature_range=(-1, 1))
        scl.fit(img)
        n_img = scl.transform(img)
        n_img_arr.append(n_img)
    bw_img_arr = n_img_arr
    print(bw_img_arr)
        
    return bw_img_arr