""" helper to deal with all operations on the received request/tweet"""

import re

class ResourceRequest:
    
    def __init__(self,Tweet):
        self.id = Tweet.id
        self.tweet = Tweet.text.lower() #Tweet object from tweepy in lowercase
        self.verified = True 
        self.required = False
    
    @property
    def help_message(self): #reply with default message if request is not structured properly
        return  "your request wasn't formed properly, try following some of the below guidelines"
    
    def check_params(self): #check for legitimate params
        try:
            tweet = re.sub(' ','',self.tweet)
            pattern = re.compile("@([a-zA-Z0-9]+)(\([a-zA-Z]+\))\(.+\)((\([a-zA-Z]+\))?)+")
            print("pattern matched:", re.match(pattern,tweet).group())
            return True
        
        except Exception as e:  
            print(self.tweet)
            return False
    
    def extract_params(self): #tokenize request
        if self.check_params():
            try:
                res = re.findall(r'\(.*?\)', self.tweet)
                res = [re.sub('[()]','',item).split(',') for item in res]
            except:
                return "could not extract parameters even though the request was formed properly, please inform the devs"
            return res
        else:
            return self.help_message

if __name__ == "__main__":
    pass



