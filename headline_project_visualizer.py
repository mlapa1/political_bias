# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:33:44 2021

@author: mlapa
"""

import csv
import numpy as np
from nltk.tokenize import word_tokenize
from train_naive_bayes import train_naive_bayes
import matplotlib.pyplot as plt

# In this part, we plot the average test set accuracy vs. the training set 
# size, where the average is taken over 20 choices of the random seed used
# to shuffle the data before splitting it into train and test sets.
    
# n_each_values = np.array([350, 375, 400, 425, 450])
# random_seeds = [i for i in range(20)]

# test_accuracy_mean = []
# test_accuracy_std = []

# for n_each in n_each_values:
#     temp = np.zeros(len(random_seeds))
#     for i, random_seed in enumerate(random_seeds):
#         temp[i] = train_naive_bayes(n_each, random_seed)
        
#     test_accuracy_mean.append(np.mean(temp))
#     test_accuracy_std.append(np.std(temp))


# # We visualize the standard deviation of the test set accuracy (for each 
# # training set size) by using a plot with error bars.
# fig, ax = plt.subplots()
# ax.errorbar(2 * n_each_values, test_accuracy_mean, xerr = 0, yerr = test_accuracy_std, ecolor = 'k', capsize = 5, linestyle = 'dotted', color = 'k', marker = 'o', markersize = 3, mfc = 'r', mec = 'r')
# ax.annotate(round(test_accuracy_mean[-1], 3), (2 * n_each_values[-1] + 2, test_accuracy_mean[-1]), fontsize = 8)
# plt.axis([675, 925, 0, 1])
# plt.xlabel('Size of training set')
# plt.ylabel('Test set accuracy')
# plt.show() 

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# In this part, we visualize the frequencies for the most commonly occuring 
# words in our headline data set. 

# Make a dictionary 'frequencies' where each key is a tuple of the form 
# (word, label), where 'word' is a word from a headline and 'label' is a 0 
# or 1. The value corresponding to this key will be set equal to the 
# number of times the pair occurs in the entire corpus.
frequencies = {}
# Make a dictionary 'overall_frequencies' whose keys will be words and whose
# values will be the number of occurences of that word in the entire 
# corpus.
overall_frequencies = {} 

# Read from the cleaned data to fill the frequencies and overall_frequencies 
# dictionary.
with open('cleaned_headline_data.csv', mode = 'r', encoding = 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for i, line in enumerate(csv_reader):
        if any(line) and (i > 0):
            # Tokenize the cleaned headline.
            tokenized_headline = word_tokenize(str(line[0]))
            label = int(line[1])
        
            for word in tokenized_headline:
                # Update frequencies.
                if (word, label) not in frequencies:
                    frequencies[(word, label)] = 1
                else:
                    frequencies[(word, label)] += 1
                
                # Update overall_frequencies.
                if word not in overall_frequencies:
                    overall_frequencies[word] = 1
                else:
                    overall_frequencies[word] += 1

# Obtain the 20 most commonly occuring words in the corpus and store them in 
# a list called 'most_used_words'.
word_list = list(overall_frequencies.keys())
word_counts = list(overall_frequencies.values())
indices = np.argsort(word_counts)
indices = np.flip(indices)
most_used_words = []

for i in indices[:20]:
    most_used_words.append(word_list[i])

# Display the 20 most used words, with the first word being the most
# commonly occuring one.
print(most_used_words)

# For each word in most_used_words, count the number of occurences of that
# word in the left- and right-leaning headlines. Store that information
# in the list 'data'.
data = []

for word in most_used_words:
    left_count = frequencies.get((word, 0), 0)
    right_count = frequencies.get((word, 1), 0)
    
    data.append([word, left_count, right_count])

# Make a scatter plot of the 20 most commonly occuring words, in which the
# x and y coordinates of each word are the number of occurences of that word
# in the left- and right-leaning headlines, respectively.  
fig, ax = plt.subplots() 
left_counts = [row[1] for row in data]
right_counts = [row[2] for row in data]
ax.scatter(left_counts, right_counts, color = 'b', marker = '.')  
plt.xlabel("# of appearances in left-leaning sources")
plt.ylabel("# of appearances in right-leaning sources")

# Label each data point with the word that it represents.
for i in range(len(data)):
    ax.annotate(data[i][0], (left_counts[i] + 1, right_counts[i] + 1), fontsize = 8)

# Plot a red line on the diagonal
ax.plot([0, 80], [0, 80], color = 'red') 
plt.axis([0, 80, 0, 80])
plt.show()   
    
    
    



