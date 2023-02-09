# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 06:27:14 2023

@author: SAMSUNG
"""
from black_and_white_system import black_and_white_converter

#group an entire image list to batches
def make_batch():
    img_arr = black_and_white_converter()
    print(img_arr)
    print('\nin make_batch, ', img_arr, 'is it')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, ', img_arr, 'is it')
    batched_list = []
    for i in range(len(img_arr)-62):
        a_batch = []
        a = 1
        while a < 62:
            a_batch.append(img_arr[i+a])
            a += 1
        batched_list.append(a_batch)
    return batched_list