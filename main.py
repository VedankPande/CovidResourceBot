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
    # request = "@ResourceBot (poone)  (oxygen,remdesivir,bed,food,ambulance) (extraargs)"
    # params = [['poone','moombai'],['oxygen','remesdesvir','bed','food','ambulance'],['vedank']]
    # print(tune(params))
    # generator = LinkGen()
    # print(generator.generate_link(tune(params)))

    # request = '''Your request isn't formed properly, please try some of the below guidlines: \n
    #                 1. A request has 4 parts (city)(resources)(negation words)(provide)\n
    #                     the last two are optional\n
    #                 2. Ensure that each part of your request is enclosed between parenthesis ()\n
    #                 3. If you use the optional provide request, ensure that it is placed at\n
    #                     the end of your request\n
    #                 4. It is mandatory for separate words in the resources part to be \n
    #                     separated by commas'''
    # gen = LinkGen()
    # print(gen.generate_link(tune(request)))

    api = Api(consumer_key,consumer_secret,access_token,access_token_secret,since_id)



    while(True):
        time.sleep(30)
        api.mentions_timeline()



