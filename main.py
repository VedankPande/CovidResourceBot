from test import generate_link
from resourcebot.generate_links import LinkGen
from resourcebot.RequestHelper import ResourceRequest
from resourcebot.TweepyWrapper import Api
from resourcebot.autocorrect import find_match,correct,tune
from resourcebot.autocorrect import add_alternatives

import time
import re
# sample search param format: City (comma separated requirements) optional params: 'verified'  change later 

consumer_key = "2Fa0aWQL6Jlyfx0vP2l6ROwIv"
consumer_secret = "W0DCBRmLRL9m0r1RNIvr7vFUX1VikeFmhSvuqGxMJA5fsB3f2I"
access_token = "896024023531913217-9UYqVvatdCsoOzLDJZlY8i6oIECD3ER"
access_token_secret = "fr1dHeiyOoQZC0BgGrVUnzPwBne7uUyO2dO7DILASLhpX"
since_id =1392801506370277384

# def check_params(text): #check for legitimate params

#     try:
#         text = re.sub(' ','',text)
#         pattern = re.compile("@([a-zA-Z0-9]+)(\([a-zA-Z]+\))\(.+\)((\([a-zA-Z]+\))?)+")
#         print("pattern check", re.match(pattern,text).group())
#         return True
    
#     except Exception as e:  
#         return False

# def extract_params(text): #tokenize request

#     if check_params(text):
#         try:
#             res = re.findall(r'\(.*?\)', text)
#             res_list = [re.sub('[()]','',item).split(',') for item in res]
#         except:
#             return "could not extract parameters even though the request was formed properly, please inform the devs"
#         return res_list
#     else:
#         return "fooked"


if __name__ == "__main__":
    # request = "@ResourceBot (poone)  (oxygen,remdesivir,bed,food,ambulance) (extraargs)"
    # params = [['poone','moombai'],['oxygen','remesdesvir','bed','food','ambulance']]
    # res = extract_params(request)
    # print(tune(res))

    api = Api(consumer_key,consumer_secret,access_token,access_token_secret)



    while(True):
        time.sleep(30)
        api.mentions_timeline()



