# import re 
# import tweepy 
# from tweepy import OAuthHandler 
# from textblob import TextBlob 
# from textblob.sentiments import NaiveBayesAnalyzer

# from flask import Flask, render_template , redirect, url_for, request



# def clean_tweet( tweet): 

#         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 
         
# def get_tweet_sentiment( tweet): 
        
#         # analysis = TextBlob(clean_tweet(tweet), analyzer=NaiveBayesAnalyzer()) 

#         # if analysis.sentiment.classification == "pos": 
#         #     return 'positive'
#         # elif analysis.sentiment.classification == "neg": 
#         #     return 'negative'

#         analysis = TextBlob(clean_tweet(tweet)) 
#         if analysis.sentiment.polarity > 0:
#             return "positive"
#         elif analysis.sentiment.polarity == 0:
#             return "neutral"
#         else:
#             return "negative"


# def get_tweets(api, query, count=5): 
        
#         count = int(count)
#         tweets = [] 
#         try: 
            
#             fetched_tweets = tweepy.Cursor(api.search, q=query, lang ='en', tweet_mode='extended').items(count)
            
#             for tweet in fetched_tweets: 
                
#                 parsed_tweet = {} 

#                 if 'retweeted_status' in dir(tweet):
#                     parsed_tweet['text'] = tweet.retweeted_status.full_text
#                 else:
#                     parsed_tweet['text'] = tweet.full_text

#                 parsed_tweet['sentiment'] = get_tweet_sentiment(parsed_tweet['text']) 

#                 if tweet.retweet_count > 0: 
#                     if parsed_tweet not in tweets: 
#                         tweets.append(parsed_tweet) 
#                 else: 
#                     tweets.append(parsed_tweet) 
#             return tweets 
#         except tweepy.TweepError as e: 
#             print("Error : " + str(e)) 

# app = Flask(__name__)
# app.static_folder = 'static'

# @app.route('/')
# def home():
#   return render_template("index.html")

# # ******Phrase level sentiment analysis
# @app.route("/predict", methods=['POST','GET'])
# def pred():
# 	if request.method=='POST':
#             query=request.form['query']
#             count=request.form['num']
#             fetched_tweets = get_tweets(api,query, count) 
#             return render_template('result.html', result=fetched_tweets)

# # fetched_tweets
# # [
# #   {"text" : "tweet1", "sentiment" : "sentiment1"},
# #   {"text" : "tweet2", "sentiment" : "sentiment2"},
# #   {"text" : "tweet3", "sentiment" : "sentiment3"}
# # ]

# # *******Sentence level sentiment analysis
# @app.route("/predict1", methods=['POST','GET'])
# def pred1():
# 	if request.method=='POST':
#             text = request.form['txt']
#             blob = TextBlob(text)
#             if blob.sentiment.polarity > 0:
#                 text_sentiment = "positive"
#             elif blob.sentiment.polarity == 0:
#                 text_sentiment = "neutral"
#             else:
#                 text_sentiment = "negative"
#             return render_template('result1.html',msg=text, result=text_sentiment)


# if __name__ == '__main__':
    
#     consumer_key = 'waVpaLs0R2sPLtYnYmgfE2ZQr'
#     consumer_secret = 'z244bAN3czgCot6gNrUzQ2xe2tqzgPyPDAq78IkYlGI6dYoZuz'
#     access_token = '1415513832882069505-FUlWzzElakD1fBSTjjUHmPM10F9Vzg'
#     access_token_secret = 'k2i4zCDZrqo7JUV9gcrZCTcQKsR6qMN4RZ4mzrVVnHFOY'

#     try: 
#         auth = OAuthHandler(consumer_key, consumer_secret)  
#         auth.set_access_token(access_token, access_token_secret) 
#         api = tweepy.API(auth)
#     except: 
#         print("Error: Authentication Failed") 

#     app.debug=True
#     app.run(host='localhost')


import http.client
import json
import re


from flair.models import TextClassifier
from flair.data import Sentence
from textblob import TextBlob

# import pandas as pd
# import numpy as np
# import re
# import nltk
# from nltk.corpus import stopwords

# from keras.preprocessing.text import one_hot
# from keras.preprocessing.sequence import pad_sequences
# from keras.models import Sequential
# from keras.layers.core import Activation, Dropout, Dense
# from keras.layers import Flatten
# from keras.layers import GlobalMaxPooling1D
# from keras.layers.embeddings import Embedding
# from keras.preprocessing.text import Tokenizer

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    print("#################")
    print(tweet)
    
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    #create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    #analysis = TextBlob(tweet)

    #set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# def predict_sentiment(tweet):
#     model = Sequential()
#     instance = tokenizer.texts_to_sequences(instance)

#     flat_list = []
#     for sublist in instance:
#         for item in sublist:
#             flat_list.append(item)

#     flat_list = [flat_list]

#     instance = pad_sequences(flat_list, padding='post', maxlen=maxlen)

#     print(model.predict(instance))

conn = http.client.HTTPSConnection("api.twitter.com")
key = api_key = 'waVpaLs0R2sPLtYnYmgfE2ZQr'
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF2yYwEAAAAA3yJNIbNKWWV24mbB%2FhpE%2BQXWuuM%3DLXdMfVIeGSGbKPxcfSi2o0sEPpjFK6NZ2flgfXwbOi22ylgYxw'
}
payload = {}
params = '/2/tweets/search/recent?query=uda'


conn.request("GET", params, payload, headers=headers)

response = conn.getresponse()

try:
    data = json.load(response)
    tweets = data['data']

    for tweet in tweets:
        tweet_sentiment = get_tweet_sentiment(tweet["text"])
        #predict_sentiment(tweet["text"])
        print(tweet_sentiment)

except ValueError:
    print(ValueError)




	# def get_tweets(self, query, count = 10):
	# 	'''
	# 	Main function to fetch tweets and parse them.
	# 	'''
	# 	# empty list to store parsed tweets
	# 	tweets = []
    #     # Classify tweet['text'] using Ref: https://realpython.com/python-nltk-sentiment-analysis/





