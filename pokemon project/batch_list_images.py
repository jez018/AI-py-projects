# -*- coding: utf-8 -*-
"""
grouping an entire image to batches
Created on Wed Jan 25 13:05:37 2023

@author: SAMSUNG
"""
def batch_list_images(img_arr):
    #group an entire image list to batches
    batched_list = []
    for i in range(len(img_arr)-62):
        a_batch = []
        a = 1
        while a < 62:
            a_batch.append(img_arr[i+a])
            a += 1
        batched_list.append(a_batch)
    return batched_list