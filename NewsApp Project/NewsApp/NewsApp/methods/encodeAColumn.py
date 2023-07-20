# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:10:48 2021

@author: Abdulmalik Abubakar
"""

#There are parts of this code that i do not understand and thus must understand it before moving further
#It will be indicated with #---DNU -meaning do not understand
def encodeAColumn(column):
    print('---inside encodeAColumn')
    for i in column.index:
        print('current column:: ', column[i])
        if column[i] == 'nan':
            column[i] = 'nill'
        print('current column type: ', str(column[i]).encode('utf-8'))

        toConvert = str(column[i])
        toConvert = toConvert.encode('utf-8')
        toConvert = int.from_bytes(toConvert, 'little') #---DNU
        column[i] = toConvert
    print(column)
    return True