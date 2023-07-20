# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:32:12 2021

@author: Abdulmalik Abubakar
"""

#imports necessary libraries
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import os
import random
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import FeatureHasher
from nltk.corpus import stopwords