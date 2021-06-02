"""wrapper class for the tweepy module"""
import tweepy
from .RequestHelper import ResourceRequest
from .autocorrect import tune
from .generate_links import LinkGen

#test wrapper for Tweepy API to make the code cleaner
#all required tweepy functions should pass through this class


class Api:
    def __init__(self,consumer_key, consumer_secret, access_token, access_token_secret,since_id):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.since_id = since_id

    #twitter api object for class
    @property
    def api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)   
        return tweepy.API(auth)

    #reply to tweet
    def reply(self,parameters,id):
        self.api.update_status(status = parameters,in_reply_to_status_id = id, auto_populate_reply_metadata=True)

    #loop through mentions and perform actions
    def mentions_timeline(self):
        print("in mentions")
        for mentions in tweepy.Cursor(self.api.mentions_timeline,since_id = self.since_id).items():
            test = ResourceRequest(mentions)
            try:
                #self.reply(test.extract_params(),mentions.id)
                generator = LinkGen()
                params = test.extract_params()
                print(params)

                if type(params)==list:
                    self.reply(generator.generate_link(tune(params)),test.id)
                else:
                    self.reply(params,test.id)

            except Exception as e:
                print(e)
            self.since_id = mentions.id
            # print(test.extract_params())

    def get_mentions(self):
        for mentions in tweepy.Cursor(self.api.mentions_timeline,since_id =1392801506370277384).items():
            test = ResourceRequest(mentions)
            pass
    
    #TODO: loop through mentions cursor and validate+reply to tweets
    def reply_to_mention(self):
        pass


if __name__ == "__main__":
    pass