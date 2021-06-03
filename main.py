from resourcebot.generate_links import LinkGen
from resourcebot.TweepyWrapper import Api
from resourcebot.autocorrect import tune

import time

consumer_key = "2Fa0aWQL6Jlyfx0vP2l6ROwIv"
consumer_secret = "W0DCBRmLRL9m0r1RNIvr7vFUX1VikeFmhSvuqGxMJA5fsB3f2I"
access_token = "896024023531913217-9UYqVvatdCsoOzLDJZlY8i6oIECD3ER"
access_token_secret = "fr1dHeiyOoQZC0BgGrVUnzPwBne7uUyO2dO7DILASLhpX"
since_id =1392801506370277384



if __name__ == "__main__":

    api = Api(consumer_key,consumer_secret,access_token,access_token_secret,since_id)

    while(True):
        time.sleep(30)
        api.mentions_timeline()



