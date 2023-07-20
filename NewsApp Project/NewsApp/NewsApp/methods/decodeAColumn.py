# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:12:48 2021

@author: Abdulmalik Abubakar
"""

def decodeAColumn(column):
    print('---inside decodeAColumn')
    for i in column.index:
        toConvert = column[i]
        toConvert = toConvert.to_bytes((toConvert.bit_length() + 7) // 8, 'little')
        toConvert = toConvert.decode('utf-8')
        column[i] = toConvert
    return True