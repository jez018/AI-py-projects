import numpy

def predictNewData(toPredict, clf):
    clfyr = clf
    print('\n')
    print('---Inside predictNewData')
    #collects the count of the df(toPredict) and save it in a variable
    count = toPredict['title'].count()
    print(count)
    counter = 0
    list_dict_holder = []
    #create a while loop:
    while count > counter:
        #predict the output using the clf providing each indexed input according to the loop
        #curr_pred = clf.predict(toPredict.iloc[counter].reshape(1, -1))
        #dataToPred = [[toPredict['author'][counter], toPredict['title'][counter], toPredict['description'][counter], toPredict['source.name'][counter]]]
        #dataToPred = numpy.array([[toPredict['author'][counter], toPredict['title'][counter], toPredict['description'][counter], toPredict['source.name'][counter]]]);
        curr_pred = clfyr.predict([[toPredict['author'][counter], toPredict['title'][counter], toPredict['description'][counter], toPredict['source.name'][counter]]])
        #create a dic that holds all the output as well as the index of each of the predicted.(NB: the dic should be defined outside the loop)
        list_dict_holder.append(curr_pred[0])
        counter += 1
    print('Done with predictNewsData')
    print('\n')
    print('curr_pred ##**To be deleted later')
    print(list_dict_holder)
    return list_dict_holder #return the dictionary