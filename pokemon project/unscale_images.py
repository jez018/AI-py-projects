# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 06:31:15 2023

@author: SAMSUNG
"""

def unscale_images():
    unscaled_img= []
    #this loop unscale the values 
    for imgs in sample_images:
        for img in imgs:
            img = img.detach().cpu().numpy()
            img = img.reshape((28, 28))
            img = scl.inverse_transform(img)
            unscaled_img.append(img)