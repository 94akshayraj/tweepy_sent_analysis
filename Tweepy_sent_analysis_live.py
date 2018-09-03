import tweepy
from textblob import TextBlob

consumer_key = 'WbKHRHFIVCaoSHTazOoyMXafJ'
consumer_secret = 'vE0UGUpvOwkLBK4c7pIjQzpSQuIQQ3Z5pzZLb8MCbNYVsJqEou'

access_token = '585332053-X0z3nKOE3PiyGPO29KHewFWe0Je3lq3GSA0cBHzc'
access_token_secret = 'cOSUlog6IIwfTiqACmJ0jAFeGTQp1Uk2uUUJNm4sn10Yv'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
