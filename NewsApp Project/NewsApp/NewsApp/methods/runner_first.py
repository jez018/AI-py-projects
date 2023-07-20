

from.getJsonNewsData import getJsonNewsData
from.collAndStore import collAndStore
from .loadAndAppend import loadAndAppend
from.loadAndFeedLikes import loadAndFeedLikes
from .trainModelAndPredict import trainModelAndPredict
from django.http import JsonResponse
from .assignID import assignID
import pandas as pd

url = 'https://newsapi.org/v2/top-headlines?country=ng&apiKey=002648d343624364a759bffc6ec6c009'
url2 = 'https://api.github.com'

#This variables are to be del when app is finished then user_status parameter argument is gotten from phone
user_status = 'first_timer'
user_status2 = 'second_timer'

def runner(request, url_path = url, user_status=user_status):
    print('*#*#*#*#----- STARTING RUNNER -----#*#*#*#*')
    print('User Status: ', user_status)

    jsonObject = getJsonNewsData(request, url_path)

    if(user_status == 'first_timer'):
        collAndStore(jsonObject)
        df = pd.read_csv('news_data.csv')
        assignID(df)

    if(user_status == 'second_timer'):
        loadAndAppend(jsonObject)

    jsonObject = loadAndFeedLikes() #This returns json object

    return trainModelAndPredict(jsonObject)
    #return JsonResponse(jsonObject)