# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:50:44 2023

@author: SAMSUNG
"""

def data_collection():
    sms_raw = pd.read_csv('spam.csv', encoding='ISO-8859-1')
    return sms_raw

def data_preprocess(sms_raw):
    sms_raw = sms_raw[['v1', 'v2']]
    sms_raw['spam'] = sms_raw['v1']
    sms_raw['message'] = sms_raw['v2']
    sms_raw = sms_raw[['spam', 'message']] 
    return sms_raw

def info(sms_raw):
    print('\nDiscription: ', sms_raw.describe())
    print('\nFirst five values of the dataset: ', sms_raw.head())
    print('\nValue Counts: ', sms_raw.value_counts())
    print('\nShape of dataset: ', sms_raw.shape)
    print('\nSample of message: ', sms_raw.iloc[77].message)

##### Im not sure about this piece of code, i need to look into though
spark = ps.sql.SparkSession.builder.master('local[4]').appName('spark_ml').getOrCreate()
sc = spark.sparkContext

n = 5572

def grouping(sms_raw):
    grouping_df = sms_raw.groupby('spam')
    print('grouping sample: ', grouping_df.first())
    return grouping_df

def spam_group(grouping_df):
    #this cell gathers the only the sam dataframe and presents it
    from pandas import DataFrame
    spam = grouping_df.get_group('spam') #this code here grabs the spam data from the general df
    spam_df = DataFrame(spam) #makes sure its converted to a df
    spam_df = spam_df.reset_index(drop = True) #this code resets the index and arranges it in order at the samme time deleting the previoous index
    return spam_df

def filt():
    frq_verbs = ['be',
    'have',
    'do',
    'say',
    'get',
    'make',
    'go',
    'know',
    'take',
    'see',
    'come',
    'think',
    'look',
    'want',
    'give',
    'use',
    'find',
    'tell',
    'ask',
    'work',
    'seem',
    'feel',
    'try',
    'to','in','or','our',
    'leave',
    'call']
    n = 747
    i = 0
    while i < n:
        for frq in frq_verbs:
            #sms_raw.iloc[i].message(' '+frq+' ', case=False)
            #spam_df.iloc[i].message = spam_df.iloc[i].message.replace(' %s '% (frq), "") #.message.str.contains(' '+frq+' ', case=False)
            spam_df.message[i] = spam_df.message[i].replace(' %s '% (frq), ' ')
            print('valid', "    ---",frq,"---    ", " -",i,"- ", spam_df.iloc[i].message)
        else:
            print('invalid')
        i = i + 1

def gathering_prioritizing_appe():
    #gathering the words and prioritising them based on appearance
    
    n = 747
    rdd_1 = (sc.parallelize(range(n)).map(lambda a : spam_df.message[a]).flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1 + count2)).collect()#reduceByKey(lambda count1, count2: count1 + count2)).collect() #.map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1+count2)).collect()
    prir_df = pd.DataFrame(rdd_1, columns=["words", "occurance"])
    
    new_prir_df = prir_df
    
    def red_prir_df(i):
        for x in i:
            if prir_df['occurance'][x] < 10 :
                new_prir_df.drop([x], inplace=True) 
                print('deleted ', x)
            else:
                print('passed ', x)
    red_prir_df(new_prir_df.index)
    new_prir_df.reset_index(inplace = True)
    new_prir_df = new_prir_df[['words', 'occurance']]
    new_prir_df_words = new_prir_df['words']
    new_prir_df_words = new_prir_df_words.to_list()
    analysis_df = pd.DataFrame()
    for i in new_prir_df_words:
        analysis_df[i] = 0
    print('done with gathering_prioritizing_appe')
    return prir_df, new_prir_df_words

def grp(sms_raw):
    #More indepth grouping
    grp = sms_raw.groupby(sms_raw.spam)
    
    spam_data = grp.get_group('spam')
    ham_data = grp.get_group('ham')
    
    spam_data.reset_index(inplace=True)
    del spam_data['index']
    
    ham_data.reset_index(inplace=True)
    del ham_data['index']
    
    del spam_data['spam']
    del ham_data['spam']

def filler(select):
    selector = select
    for word in new_prir_df_words:
        for i in spam_df.index:
            if selector == 'spam':
                if word in spam_data.message[i].split():
                    a[word].iloc[0] += 1
            elif selector == 'ham':
                if word in ham_data.message[i].split():
                    a[word].iloc[1] += 1
                    
def filtering_hard_way():
    #filtering the hard way
    n=4288
    i = 0
    while i < n:
        if prir_df.occurance[i] < 20:
            prir_df.drop(i, inplace=True)
            #print("droped...")
        i = i + 1
    print('dropped all successfuly')
    print('Total count of dropped: ', i)

def new_df_creation_and_train_test_df():
    #creating new df for using selected words as columns
    keywords_df = sms_raw
    keywords_df = pd.DataFrame(keywords_df) 
    keywords_df.drop(columns=['message'], inplace=True)
    
    #creation of the columns of the new df process and assigning it its values for further applying ML algorithms 
    for i in prir_df.words:
        keywords_df[i] = sms_raw.message.str.contains(' '+i+' ', case=False)
    
    print('\nDiscription of the created df: ', keywords_df.describe()) 

    #seperating X and y for training
    X = keywords_df.drop(columns=['spam'])
    y = keywords_df.spam
    
    return X, y

def training(X, y):
    #imorting necessary libraries for the bellow 
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    
    #splitting the records into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    
    #innitiating the classifier
    clf = SVC()
    
    #fiiting or training the data
    clf.fit(X_train, y_train)
    
    #fiiting or training the data
    clf.fit(X_train, y_train)
    
    print('Done training...')
    
    #checking for the accuracy
    #print('Accuracy: ', clf.score(X_test, y_test))
    
    y2_pred = clf.predict(X_test)
    y2_pred = DataFrame(y2_pred)
    
    print('All Done::::::')
    print('Displaying confusion matrix')
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, y2_pred)
    print(confusion_matrix(y_test, y2_pred))
    
def main():
    sms_raw = data_collection()
    sms_raw = data_preprocess(sms_raw)
    info(sms_raw)
    grouping_df = grouping(sms_raw)
    spam_df = spam_group(grouping_df)
    filt()
    prir_df, new_prir_df_words = gathering_prioritizing_appe()
    grp(sms_raw)
    filler(select = 'spam')
    filler(select = 'ham')
    filtering_hard_way()
    X, y = new_df_creation_and_train_test_df()
    training(X, y)
    print('End of main')
    
    