from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
#from requests import *
#import urllib3
from django.http import HttpResponse
from django.http import JsonResponse

#import
#from snippets.serializers import SnippetSerializer


def test101(request):
    url = 'https://newsapi.org/v2/top-headlines?country=ng&apiKey=002648d343624364a759bffc6ec6c009'
    #request_url = urllib.request.urlopen(url)
    data = requests.get(url)
    #http = urllib3.PoolManager()
    #data = get('GET', url)
    print(data.json())
    #print(dir(requests)) #

    print(' ')
    print(' ')
    print(' ')
    #print(data.json())
    #return Response(data.json)
    #return json.dumps(data)
    return JsonResponse(data.json())