# political_bias
Can you guess the political leanings of a news source from a headline?

In this project we will construct classifiers that attempt to guess the political leanings of a news source from the text of a headline. Our political setting is the United States of America in the year 2021, and all of our results should be viewed in that context. To determine the political leanings of a news source we rely on the Media Bias Chart from ad fontes media:

https://www.adfontesmedia.com/

In fact, this chart contains much more information than we need here. We only use it to classify a news source as left- or right-leaning (the horizontal axis of the chart). For example, the chart classifies The New York Times to be slightly left of center and The Wall Street Journal to be slightly right of center.

To train our classifiers we used the free version of News API (newsapi.org) to obtain 100 headlines each from five left-leaning sources and five right-leaning sources (using
the Media Bias Chart to determine the leanings of each source), for a total of 1000 headlines. It would be nice to have more data but the free version of News API seems to only allow a download of 100 articles from each source on any given day (and the news cycle moves so fast that it would be ideal to update the data each day). The five left-leaning news sources that we used were:

washingtonpost.com, cnn.com, msnbc.com, huffpost.com, and jezebel.com.

The five right-leaning news sources that we used were:

wsj.com, reason.com, foxnews.com, nationalreview.com, and dailywire.com.

In the file retrieve_headline_data.py we obtained the raw data from these sources on 4/1/2021 and saved it to the file headline_data.csv, along with the labels for each headline (left = 0 and right = 1). In the file headline_data_cleaner.py we applied standard text cleaning techniques (make lowercase, remove stopwords, remove punctuation and numbers, stem the words, etc.) to the text of each headline, and saved the resulting data in the file cleaned_headline_data.csv. The figure top_20_words.pdf is a visualization of the 20 most frequently occuring words in our cleaned headline data, with each word plotted as a point in a 2D plane with the x and y coordinates equal to the number of occurences of each word in the left- and right-leaning headlines in our data set. The top 20 words in our cleaned data set (in descending order of most frequently occuring) were:

biden, say, covid, new, vaccin, trump, us, report, plan, vote, law, gop, infrastructur, call, georgia, border, state, gaetz, bill, hous

In the file train_naive_bayes.py we train a naive Bayes classifier on this data set (following part 1 of Coursera's Natural Language Processing specialization) and check its accuracy on a hold-out test set. In the figure test_set_accuracy.pdf we plot the test set accuracy vs. the size of the training set. Each point in that plot represents the
average test set accuracy for 20 different values of the random seed used to shuffle the data before dividing it into training and test sets. The error bars show the standard
deviation of the test set accuracy. We can see that with the largest training set size this classifier achieved an average test set accuracy of 65.7%, which is not bad 
considering the difficulty of the task, the relatively small size of the data set, and the simplicity of the naive Bayes classifier.

In the future we hope to apply more sophisticated techniques to this problem, for example adapting the neural network techniques that are used for more advanced sentiment analysis tasks.



