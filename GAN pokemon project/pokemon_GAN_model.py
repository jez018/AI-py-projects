# -*- coding: utf-8 -*-
"""
Pokemon GAN
Created on Tue Jan 24 07:15:19 2023

@author: SAMSUNG
"""

import torch.nn as nn
import torch.nn.functional as F
import torch

#from initialization_file import dis, gen, l_v, l_v_input, batch_size

#discriminator
class D(nn.Module):
    def __init__(self, input_l, output_l_d, hidden_dim):
        super(D, self).__init__()
        self.fc1 = nn.Linear(input_l, hidden_dim*2)
        self.fc2 = nn.Linear(hidden_dim*2, hidden_dim*4)
        self.fc3 = nn.Linear(hidden_dim*4, hidden_dim*2)
        self.fc4 = nn.Linear(hidden_dim*2, output_l_d)
        
        #defining the dropout
        self.dropout = nn.Dropout(0.3)
    def forward(self, x):
        #print('picture shape: ', x.size())
        # flatten image
        x = x.view(-1, 28*28).to(torch.float32)
        #print(x)
        
        x = self.dropout(F.leaky_relu(self.fc1(x), 0.2))
        x = self.dropout(F.leaky_relu(self.fc2(x), 0.2))
        x = self.dropout(F.leaky_relu(self.fc3(x), 0.2))
        
        #No activation function for the last layer
        output = self.fc4(x)
        #print('output_shape: ', output.shape)
        #print('output: ')
        #print(output)
        
        return output
        

#generator
class G(nn.Module):
    def __init__(self, input_l, output_l_g, latent_v, hidden_dim):
        super(G, self).__init__()
        self.fc1 = nn.Linear(input_l, hidden_dim*2)
        self.fc2 = nn.Linear(hidden_dim*2, hidden_dim*4)
        self.fc3 = nn.Linear(hidden_dim*4, hidden_dim*2)
        self.fc4 = nn.Linear(hidden_dim*2, output_l_g)
        
        #dropout
        self.dropout = nn.Dropout(0.3)
        
    def forward(self, latent_v):
        x = latent_v
        x = x.view(-1, 100).to(torch.float32)
        #print(input_l)
        #print(x)
        x = self.dropout(F.leaky_relu(self.fc1(x), 0.2))
        x = self.dropout(F.leaky_relu(self.fc2(x), 0.2))
        x = self.dropout(F.leaky_relu(self.fc3(x), 0.2))
        
        #tanh activation function for the last layer
        output = F.tanh(self.fc4(x))
        return output