import tweepy
import os
import time

class SpamTwitter:
    request_limit = 20
    twitterApi = ""

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
        while True:
            message = "@instagram, user @dejimarquis has an issue that they need your help debugging, but they haven't gotten any response from the team. " +
            "They have sent emails, used the report an issue button on the app and even sent multiples tweets to you. Please who can help? To reach out, DM @dejimarquis"
            self.tweet(message)
            time.sleep(60 * 60 * 60)

if __name__ == '__main__':
    client = SpamTwitter()
    client.spam()