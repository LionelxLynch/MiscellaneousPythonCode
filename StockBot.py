import secrets
import tweepy

key = '1500629496864591872-mAZ0zRA1y6KZbbb2fqBjgkdKd89LgP'
secret = 'ZtuhYucakPTOr8TFYHN6hebMbH1faY1ToRIuQ7mynJ3lQ'
consumer_key = 'MU1G7LFtpLFjgLfyJcWvD8g8V'
consumer_secret = 'BEqRJdP0TVUl2g8d73giiKUmZmRW1j0qsXD3gakhQfg9oWrfTE'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('StockBOT checking in.....')