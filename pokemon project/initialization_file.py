# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 06:24:47 2023

@author: SAMSUNG
"""
from pokemon_GAN_model import D, G
import torch
import numpy as np

input_l = 28*28
l_v_input = 100
output_l_d = 1
output_l_g = 28*28
#batch_size = 61
batch_size = 16
hidden_dim = 16
#l_v = torch.rand(input_l)
l_v = torch.from_numpy(np.random.uniform(-1, 1, size=(batch_size, l_v_input)))
dis = D(input_l, output_l_d, hidden_dim)
gen = G(l_v_input, output_l_g, l_v, hidden_dim)
print(dis)
print()
print(gen)

d_optimizer = torch.optim.Adam(dis.parameters(), lr=0.002)
g_optimizer = torch.optim.Adam(gen.parameters(), lr=0.002)