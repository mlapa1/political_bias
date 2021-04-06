# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 06:51:40 2021

@author: mlapa
"""

import json
import csv
from urllib.request import urlopen

# I ran this program and compiled my data set on 4/1/2021.

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# A function to retrieve, using News API (newsapi.org), a list of 100 
# articles from 'source', which is a string that is a web address without any
# preamble, for example 'foxnews.com'. If you want to run this code you will
# need to get your own API key from newsapi.org and enter it where I have put
# the text 'YOUR_API_KEY_GOES_HERE'.
def get_article_list(source):
    
    domain = 'domains=' + source + '&'
    
    url = ('https://newsapi.org/v2/everything?' +
       domain +
       'language=en&' +
       'pageSize=100&' +
       'page=1&' +
       'apiKey=YOUR_API_KEY_GOES_HERE')

    with urlopen(url) as response:
        source = response.read()
    
    data = json.loads(source)

    article_list = data['articles']
    
    return article_list

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# Retrieve 100 headlines for each source and write the data to a csv file.

# Left-leaning sources according to the Media Bias Chart at
# https://www.adfontesmedia.com/
sources_l = ['washingtonpost.com', 'cnn.com', 'msnbc.com', 'huffpost.com', 'jezebel.com']

# Right-leaning sources according to the Media Bias Chart at
# https://www.adfontesmedia.com/
sources_r = ['wsj.com', 'reason.com', 'foxnews.com', 'nationalreview.com', 'dailywire.com']

sources = sources_l + sources_r

# Labels for the sources with 'left' = 0 and 'right' = 1.
labels_l = [0] * len(sources_l)
labels_r = [1] * len(sources_r)

labels = labels_l + labels_r

with open("headline_data.csv", mode = "w", encoding = 'utf-8') as csv_file:
    fieldnames = ['headline_text', 'source', 'time_stamp', 'label']
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()
    
    for i, s in enumerate(sources):
        # Retrieve the data from News API.
        article_list = get_article_list(s)
        # Loop through the list of articles and write the relevant information
        # to our csv file.
        for a in article_list:
            csv_writer.writerow({'headline_text': a['title'], 'source': s, 'time_stamp': a['publishedAt'], 'label': labels[i]})
        