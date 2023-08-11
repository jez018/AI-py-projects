# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:44:22 2021

@author: Abdulmalik Abubakar
"""

init = 0
make = 0

init = eval(input('Input Init Amount: '))
make = eval(input('Input Current Made Amount: '))

prof = make - init

re_inv = (55/100)*prof
init_total = prof + init
curr_total = init_total - re_inv
touchable_prof = curr_total - init
f_total_amt = init_total - touchable_prof

print('Your Widrawable amount: ' ,touchable_prof)
