import tweepy
import time

# API login information
consumer_key = "FCFw4dWlPnPmnTdhTi2lS0njg"
consumer_secret = "cUdOXhZtax69QpuCnQ2ncF2KPcRcrlaX3KsUIZsuCf1Ah2QxHt"
access_token = "1085978848007778306-zqudyb4MNCpFQA8aB1IztGbZcrDol5"
access_token_secret = "xFMvc7M0S1aWAcgcP5qFiTXq5g01ScPXNLoo1WAHhBQdz"

# Authorization of API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Authentication
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break