from django.http import HttpResponse
#from sklearn.datasets import iris
from .methods import assesAndAssign
import pandas as pd

def test(request):
    a = 1
    b = 2
    c = a+b
    return HttpResponse('abdul{c}')

def test2(request):
    df = pd.read_csv(r'F:\Projects\NewsApp Project\Other Files\news_data2.csv')
    name = 'title'
    #return df
    assesAndAssign.assesAndAssign(df=df, nameOfMainColumn=name, request=request)
    return HttpResponse('done!')