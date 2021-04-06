# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 08:32:03 2021

@author: mlapa
"""

import csv
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# A function that cleans the text of 'headline' from 'source'.
def headline_processor(headline, source):
    
    # Dictionary of extraneous phrases that we need to discard for some of the
    # sources.
    need_to_discard = {'washingtonpost.com': ['washington post'], 'wsj.com': ['wall street journal', 'fox business']}
    
    # English stopwords
    en_stopwords = stopwords.words('english')
    
    # The order of these operations is important!
    headline = headline.lower() # Make lowercase
    headline = re.sub('-', ' ', headline) # Replace dashes with whitespace (don't want to accidentally fuse different words together)
    headline = re.sub('\s+', ' ', headline) # Remove extra whitespace
    headline = ' '.join(word for word in headline.split() if word not in en_stopwords) # Remove stopwords (the words in en_stopwords contain punctuation!)
    #headline = re.sub('[^0-9A-Za-z ]', '' , headline) #Remove punctuation
    headline = re.sub('[^A-Za-z ]', '' , headline) #Remove punctuation and numbers
    
    # Remove special words for certain sources.
    if source in need_to_discard:
        for word in need_to_discard[source]:
            headline = re.sub(word, '', headline) 
            
    # Stem the remaining words.
    stemmer = PorterStemmer()
    headline = ' '.join(stemmer.stem(word) for word in headline.split())
    
    return headline

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# Read from the raw data, clean the data, and then write the cleaned data
# to a new csv file.

# Create two Python sets called cleaned_data_set_0 and cleaned_data_set_1 
# Using these sets to hold the data will allow us to eliminate some repeated 
# headlines that may be in the raw results from News API.

cleaned_data_set_0 = set()
cleaned_data_set_1 = set()

with open('headline_data.csv', mode = 'r', encoding = 'utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    
    for line in csv_reader:
        # Process the headline text. The variable 'processed_headline' is still 
        # a string. We will not tokenize it at this point.        
        processed_headline = headline_processor(line['headline_text'], line['source'])
        
        if (processed_headline != ''):
            # Add processed_headline to the appropriate set.
            if int(line['label']) == 0:
                cleaned_data_set_0.add(processed_headline)
            else:
                cleaned_data_set_1.add(processed_headline)

# Report the number of elements in the cleaned sets.
# print(len(cleaned_data_set_0))
# print(len(cleaned_data_set_1))

# Write the cleaned data to a new file.

with open("cleaned_headline_data.csv", mode = "w", encoding = 'utf-8') as csv_file:
    fieldnames = ['cleaned_headline_text', 'label']
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()
    
    for headline in cleaned_data_set_0:
        csv_writer.writerow({'cleaned_headline_text': headline, 'label': 0})
        
    for headline in cleaned_data_set_1:
        csv_writer.writerow({'cleaned_headline_text': headline, 'label': 1})
    
    
    
        
    