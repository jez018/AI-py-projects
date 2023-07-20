# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:16:09 2021

@author: Abdulmalik Abubakar
"""
from .stringCleaner import stringCleaner

#asseser and assigner function

# def assesAndAssign(df, nameOfMainColumn, request):
#     df2 = df
#     #if request.method == 'POST':
#     for i in df2.index:
#         for word in df2[nameOfMainColumn][i].split(' '):
#             if word in df.columns:
#                 df2[word][i] = 1
#
#     df2.to_csv(r'F:\Projects\NewsApp Project\Codes setup\news_new.csv')
#     return


### StringCleaner function -- cleans the word and makes sure it isnt a stop word
# def stringCleaner(word):
#     from nltk.corpus import stopwords
#
#     word = list(word)
#     counter = 0
#     for letter in word:
#         if letter.isalpha() == False:
#             del word[counter]
#         counter += 1
#     word = ''.join(word)
#     if word not in stopwords.words():
#         return word
#     else:
#         return None

#asseser and assigner function
def assesAndAssign(df, nameOfMainColumn, request):
    print('---inside assesAndAssign')
    print('----e----')
    for i in df.index:
        for word in str(df[nameOfMainColumn][i]).split(' '):
            #print(df[nameOfMainColumn][i].split(' '))
            #stringCleaner() #code-- if code contains punctuation marks or stopwords or symbols it removes the symbols or marks and overwrite.
            word = stringCleaner(word)
            if word != None:
                if word not in df.columns:
                    df[word] = 0
                if word in df.columns:
                    df[word][i] = 1
    df.to_csv(r'F:\Projects\NewsApp Project\Codes setup\news_news_new.csv')
    return df
    #checked --status: Passed!
