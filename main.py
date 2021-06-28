from resourcebot.generate_links import LinkGen
from resourcebot.TweepyWrapper import Api
from resourcebot.autocorrect import tune

import time

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
since_id =1392801506370277384



if __name__ == "__main__":

    api = Api(consumer_key,consumer_secret,access_token,access_token_secret,since_id)

    while(True):
        time.sleep(30)
        api.mentions_timeline()



