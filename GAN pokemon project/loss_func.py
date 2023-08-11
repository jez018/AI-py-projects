# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 06:26:30 2023

@author: SAMSUNG
"""
import torch
import torch.nn as nn
#import torch.nn.functional as F

#discriminators loss
def disc_loss_for_fake_data(x, batch_size):
    labels = torch.zeros(batch_size)
    #print('loss for fake data')
    #print('size for pred_disc_l: ', x)
    #print('size for label_disc_l: ', labels)
    criterion = nn.BCEWithLogitsLoss()
    loss = criterion(x, labels)
    return loss
def disc_loss_for_real_data(x, batch_size):
    labels = torch.ones(batch_size)*0.9 #*0.9 indicates smoothing
    #print('loss for real data')
    #print(x)
    #print('size for pred_disc_l: ', x)
    #print('size for label_disc_l: ', labels)
    criterion = nn.BCEWithLogitsLoss()
    loss = criterion(x, labels)
    return loss