import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import sys, getopt
import csv

'''
for i in range(2020,2024):
    season = str(i) + '-' + str(i+1) + '/' + str(i) + '-' + str(i+1)
    url = 'https://fbref.com/en/comps/9/' + season + '-Premier-League-Stats'
    df = pd.read_html(url)
'''

df = pd.read_html('https://fbref.com/en/comps/9/2018-2019/stats/2018-2019-Premier-League-Stats')
print(df[2])
