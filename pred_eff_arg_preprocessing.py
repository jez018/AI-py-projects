# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:01:21 2022

@author: Abdulmalik Abubakar
"""

import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import nltk
import random

df = pd.read_csv('train.csv')
df.head(10)

grouped_df = df.groupby(df['discourse_type'])

Claim_df = grouped_df.get_group('Claim').sample(30)
Position_df = grouped_df.get_group('Position').sample(30)
Lead_df = grouped_df.get_group('Lead').sample(30)
Evidence_df = grouped_df.get_group('Evidence').sample(30)
Counterclaim_df = grouped_df.get_group('Counterclaim').sample(30)
Rebuttal_df = grouped_df.get_group('Rebuttal').sample(30)
Concluding_statement_df = grouped_df.get_group('Concluding Statement').sample(30)

Claim_df = Claim_df.reset_index().drop(columns=['index'])
Position_df = Position_df.reset_index().drop(columns=['index'])
Lead_df = Lead_df.reset_index().drop(columns=['index'])
Evidence_df = Evidence_df.reset_index().drop(columns=['index'])
Counterclaim_df = Counterclaim_df.reset_index().drop(columns=['index'])
Rebuttal_df = Rebuttal_df.reset_index().drop(columns=['index'])
Concluding_statement_df = Concluding_statement_df.reset_index().drop(columns=['index'])

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

print(nltk.word_tokenize("The cat is very cute"))

default_range = range(50)


#import string
#'Lead'
lead = []
for i in Lead_df.index:
    name = str(Lead_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            lead.append([format_sentence(i), 'lead'])
print('done')
position = []
for i in Position_df.index:
    name = str(Position_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            position.append([format_sentence(i), 'position'])
print('done')
concluding_statement = []
for i in Concluding_statement_df.index:
    name = str(Concluding_statement_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            concluding_statement.append([format_sentence(i), 'Concluding_statement'])
print('done')
evidence = []
for i in Evidence_df.index:
    name = str(Evidence_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            evidence.append([format_sentence(i), 'evidence'])
print('done')
counterclaim = []
for i in Counterclaim_df.index:
    name = str(Counterclaim_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            counterclaim.append([format_sentence(i), 'counterclaim'])
print('done')
rebuttal = []
for i in Rebuttal_df.index:
    name = str(Rebuttal_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            rebuttal.append([format_sentence(i), 'rebuttal'])
print('done')
concluding_statement = []
for i in Concluding_statement_df.index:
    name = str(Concluding_statement_df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    with open(f"train/{name}.txt") as f:
    #with open(f"HR_analysis/todo_steps.txt") as f:
        for i in f: 
            concluding_statement.append([format_sentence(i), 'Concluding_statement'])
print('done')

df1 = df
dfs = [Lead_df, Position_df, Claim_df, Evidence_df, Counterclaim_df, Rebuttal_df, Concluding_statement_df]
final_df = pd.concat(dfs)
df1 = final_df.reset_index().drop(columns=['index'])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#function to calculate len of each essay by words and creating a seperate dataset with the len and essay id automatically
#import string
#'Lead'
#This block of code calculates no of words in the essay

def format_sentence(words):
    return({word: True for word in words})

#This variables hold tokenized words/sentence for each of the categories
lead_bank = [] 
position_bank = [] 
claim_bank = [] 
evidence_bank = [] 
counterclaim_bank = [] 
rebuttal_bank = [] 
concluding_statement_bank = []

len_words_no_stopwords = []
len_words_with_stopwords = []
tagged_words = ()

df2 = df1#[:1000]

print('stage 0')
#for i in df.index:
count = 0
for i in df2.index:
    count += 1
    curr_str = ''
    name = str(df['essay_id'][i])
    #print(name+'.txt')
    #print(f"train/{name}.txt")
    #f_loc = f"train/{name}.txt"
    with open(f"train/{name}.txt") as f:
        for j in f:
            curr_str = curr_str + j
    curr_str = curr_str.lower()
    words = word_tokenize(curr_str)
    tagged_words = tagged_words + tuple(nltk.pos_tag(words))
    len_words_with_stopwords.append(len(words))
    if df2['discourse_type'][i] == 'Lead':
        lead_bank.append([format_sentence(words), 'Lead'])
    if df2['discourse_type'][i] == 'Position':
        position_bank.append([format_sentence(words), 'Position'])
    if df2['discourse_type'][i] == 'Claim':
        claim_bank.append([format_sentence(words), 'Claim'])
    if df2['discourse_type'][i] == 'Evidence':
        evidence_bank.append([format_sentence(words), 'Evidence'])
    if df2['discourse_type'][i] == 'Counterclaim':
        counterclaim_bank.append([format_sentence(words), 'Counterclaim'])
    if df2['discourse_type'][i] == 'Rebuttal':
        rebuttal_bank.append([format_sentence(words), 'Rebuttal'])
    if df2['discourse_type'][i] == 'Concluding Statement':
        concluding_statement_bank.append([format_sentence(words), 'Concluding Statement'])
    
    print('stage 0.1')
    for s_words in stopwords.words('english'):
        words = [value for value in words if value != s_words]
        words = [value for value in words if value != ',']
        words = [value for value in words if value != '.']
    
    len_words_no_stopwords.append(len(words))
    
    #create a for loop that creates additional features and also it should check if the feature is already there so as to
    #just input in the values using there various indexes
    #Test before anexing
    print('stage 1')
    for i in range(len(tagged_words)):
        if tagged_words[i][1] not in df2.columns:
            df2[tagged_words[i][1]] = 0
            #print('***added new feature column')
    print('count progress: ', count)
    
#write a block to calculate and input each no of taggged word in the expected column
#ddrop : discourse_id	essay_id	discourse_text	discourse_type	discourse_effectiveness
def count_words(tagged_words, desiredDF, index_a):
    #categorize each word type by storing them in a dict or tuple
    for label in desiredDF.columns:
        items = [item for item in tagged_words[:][1] if item == label] #i'm not sure this is going to work
        #items = tuple(items)
        df2[label][index_a] = len(items)
    #print('Count words executed successfuly')

def assign(d, index, df):
    #print('--------------inside assign')
    for feature in df.columns:
        df2[feature][index] = d[feature]
        
desiredDF = df2.drop(columns = ['discourse_id', 'essay_id', 'discourse_text', 'discourse_type', 'discourse_effectiveness'])
#n_tagged_words = []
word_len = 0
print('word Len is ', len(desiredDF.columns))
n_curr_str = ''
print('stage 2')
for wordSpec in desiredDF.columns:
    word_len += 1
    print('wordLen count: ', word_len)
    print(wordSpec)
    count = 0
    for i in df2['essay_id'].index:
        n_tagged_words = [] ##nn
        d = collections.defaultdict(int) #nn
        f_name = df['essay_id'][i]
        f"train/{f_name}.txt"
        with open(f"train/{name}.txt") as f:
            for j in f:
                n_curr_str = n_curr_str + j
            f.close()
        n_curr_str = n_curr_str.lower()
        n_words = word_tokenize(n_curr_str)
        n_tagged_words.append(nltk.pos_tag(n_words))
        for word, pos in n_tagged_words[0]: #nn
            d[pos] += 1
        #function to assign words
        assign(d, i, desiredDF) ##nn  #This assigns the count of each part of speech in an essay to the various label features in the df 
        count +=1
        print('c_count', count)
        #call a function here to count the words
        #count_words(tagged_words, desiredDF, i)
#After all is run save the newly formed df as a .csv file
        
desiredDF.columns

print('\n\n')
print('stage 3')
df['len_of_words_no_stopwords'] = len_words_no_stopwords #writes the len of words in a text
df['len_of_words_with_stopwords'] = len_words_with_stopwords
#df['mean_of_words'] = len_words_no_stopwords/len_words_with_stopwords
    
print('done with preprocessing!!!')