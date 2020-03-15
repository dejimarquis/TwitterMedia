import tweepy
import os
import time

class SpamTwitter:
    request_limit = 20
    twitterApi = ""

    # Apply for Twitter API access here https://developer.twitter.com/en/apply-for-access
    # insert your keys and secrets here
    twitter_keys = {
        'consumer_key': "",
        'consumer_secret': "",
        'access_token_key': "",
        'access_token_secret': ""
    }

    def __init__(self, request_limit=20):
        self.request_limit = request_limit
        self.set_up_creds()

    def set_up_creds(self):
        auth = tweepy.OAuthHandler(self.twitter_keys['consumer_key'], self.twitter_keys['consumer_secret'])
        auth.set_access_token(self.twitter_keys['access_token_key'], self.twitter_keys['access_token_secret'])
        self.twitterApi = tweepy.API(auth)

    def tweet(self, message):
        self.twitterApi.update_status(message)

    def spam(self):
        no = 0
        while True:
            no = no + 1
            message = str(no) + "<Enter Message here>"
            self.tweet(message)
            time.sleep(60 * 5) # tweets every 5 minutes

if __name__ == '__main__':
    client = SpamTwitter()
    client.spam()