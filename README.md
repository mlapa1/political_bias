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

In the file retrieve_headline_data.py we obtained the raw data from these sources on 4/1/2021 and saved it to the file headline_data.csv, along with the labels for each headline (left = 0 and right = 1). In the file headline_data_cleaner.py we apply standard text cleaning techniques (make lowercase, remove stopwords, remove punctuation and numbers, stem the words, etc.) to the text of each headline.
