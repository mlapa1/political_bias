# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:32:26 2021

@author: mlapa
"""

import csv
import random
import numpy as np
from nltk.tokenize import word_tokenize

# Train and test a naive Bayes classifier on the cleaned headline data.
# The input 'n_each' is the number of each kind of example to use in the
# training set that is constructed. The input 'random_seed' controls how the 
# data is shuffled before it is split into training and test sets. This 
# function outputs test_accuracy, which is the the accuracy of the trained 
# classifier on the test set that is constructed by the function. 
def train_naive_bayes(n_each, random_seed):
    
    # Define empty lists to hold the cleaned headline data.
    cleaned_headline_data_0 = []
    cleaned_headline_data_1 = []
    
    # Import the data.
    with open('cleaned_headline_data.csv', mode = 'r', encoding = 'utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for i, line in enumerate(csv_reader):
            if any(line) and (i > 0):
                if int(line[1]) == 0:
                    cleaned_headline_data_0.append([str(line[0]), 0])
                else:
                    cleaned_headline_data_1.append([str(line[0]), 1])
        
    
    # Randomly shuffle the data using the input 'random_seed'.
    random.seed(a = random_seed) 
    random.shuffle(cleaned_headline_data_0)
    random.shuffle(cleaned_headline_data_1)
            
    # Split the data into training and test sets that are balance in terms of
    # the number of each kind of example. The total number of examples in the
    # final training set X_train is 2 * n_each.
    X_train_0 = [row[0] for row in cleaned_headline_data_0[:n_each]]
    y_train_0 = [row[1] for row in cleaned_headline_data_0[:n_each]] 
    
    X_test_0 = [row[0] for row in cleaned_headline_data_0[n_each:]]
    y_test_0 = [row[1] for row in cleaned_headline_data_0[n_each:]]
    
    X_train_1 = [row[0] for row in cleaned_headline_data_1[:n_each]]
    y_train_1 = [row[1] for row in cleaned_headline_data_1[:n_each]]
    
    X_test_1 = [row[0] for row in cleaned_headline_data_1[n_each:]]
    y_test_1 = [row[1] for row in cleaned_headline_data_1[n_each:]]
    
    X_train = X_train_0 + X_train_1
    y_train = np.array(y_train_0 + y_train_1)
    
    X_test = X_test_0 + X_test_1
    y_test = np.array(y_test_0 + y_test_1)
    
    m = len(y_train)
    
    # Make a dictionary 'frequencies' where each key is a tuple of the form 
    # (word, label), where 'word' is a word from a headline and 'label' is a 0 
    # or 1. The value corresponding to this key will be set equal to the 
    # number of times the pair occurs in the training set.
    frequencies = {}        
    
    for i in range(m):
        # Tokenize the cleaned headline.
        tokenized_headline =  word_tokenize(str(X_train[i]))
        # Update the frequencies dictionary.    
        for word in tokenized_headline:
            if (word, y_train[i]) not in frequencies:
                frequencies[(word, y_train[i])] = 1
            else:
                frequencies[(word, y_train[i])] += 1
    
    # Number of headlines in training set from left-leaning sources (label = 0). 
    D_0 = np.sum(1 - y_train)
    # Number of headlines in training set from right-leaning sources (label = 1). 
    D_1 = m - D_0 # = np.sum(y_train)
    # The set of unique words and its size.
    vocabulary = set(pair[0] for pair in frequencies.keys())
    V = len(vocabulary)
    # Number of words in left- and right-leaning headlines.
    N_0 = 0
    N_1 = 0
    for pair in frequencies.keys():
        if pair[1] == 0:
            N_0 += 1
        else:
            N_1 += 1
    
    # We are now ready to construct the naive Bayes classifier.
    
    # First compute the log of the prior.
    log_prior = np.log(D_1) - np.log(D_0)
    
    # Next, create a dictionary to store the log likelihood for each word. The
    # log likelihood for each word will be constructed from the (regularized)
    # conditional probability for the occurence of that word in the headlines
    # from left- vs. right-leaning sources.
    log_likelihood = {}
    
    for word in vocabulary:
        frequency_0 = frequencies.get((word, 0), 0)
        frequency_1 = frequencies.get((word, 1), 0)
        
        prob_0 = (frequency_0 + 1) / (N_0 + V)
        prob_1 = (frequency_1 + 1) / (N_1 + V)
        
        log_likelihood[word] = np.log(prob_1) - np.log(prob_0)
        
    # Make predictions for the test set.
    m_test = len(y_test)
    y_predict = np.zeros_like(y_test)
    
    for i in range(m_test):
        # Tokenize the cleaned headline.
        tokenized_headline =  word_tokenize(str(X_test[i]))
        # p will be the sum of the log prior plus the log likelihoods for each 
        # word in the tokenized headline. Initialize it to log_prior.
        p = log_prior
        for word in tokenized_headline:
            p += log_likelihood.get(word, 0)
        
        if p > 0:
            y_predict[i] = 1
    
    # Compute the accuracy on the test set.
    test_accuracy = np.mean(y_predict == y_test)
    
    return test_accuracy
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

