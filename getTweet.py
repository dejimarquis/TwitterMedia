import tweepy
import MyStreamListener
import urllib.request


class TwitterClient:
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

    def process_mentions(self):
        status = self.twitterApi.mentions_timeline(count = 1)[0]

        if "get" in status.text:
            filename = status.text
            mediafile = self.retrieve_media_from_blob(filename)
            self.tweet_media(mediafile)
        else:
            self.save_media(status)

    def retrieve_media_from_blob(self, filename):
        pass

    def save_media(self, status):
        repliedStatus = self.twitterApi.get_status(status.in_reply_to_status_id)
        video_info = ""
        media_url = ""
        try:
            video_info = repliedStatus.extended_entities['media'][0]['video_info']
            media_url = video_info['variants'][0]['url']
        except:
            media_url = repliedStatus.extended_entities['media'][0]['media_url']
        
        print(media_url)
        mediafile = self.download_image(media_url)
        self.store_to_blob(mediafile)

    def download_image(self, media_url):
        extension = media_url.split(".")[3]
        mediafile = "temp_media." + extension
        urllib.request.urlretrieve(media_url, mediafile)
        
        return mediafile

    def tweet_media(self, mediafile):
        self.twitterApi.update_with_media(mediafile)


if __name__ == '__main__':
    client = TwitterClient()
    client.process_mentions()