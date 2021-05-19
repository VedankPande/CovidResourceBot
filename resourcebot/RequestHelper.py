""" helper to deal with all operations on the received request"""

import re

class ResourceRequest:
    
    def __init__(self,Tweet):
        self.id = Tweet.id
        self.tweet = Tweet.text #Tweet object from tweepy
        self.verified = True 
        self.required = False
    
    @property
    def help_message(self): #reply with default message if request is not structured properly
        return  "your request wan't formed properly, try following some of the below guidelines"
    
    def check_params(self): #check for legitimate params
        try:
            pattern = re.compile("@([a-zA-Z0-9]+) (\([a-zA-Z]+\))\(.+\)((\([a-zA-Z]+\))?)+")
            print("pattern check", re.match(pattern,self.tweet).group())
            return True
        
        except Exception as e:  
            print(self.tweet)
            return False
    
    def extract_params(self): #tokenize request
        if self.check_params():
            try:
                res = re.findall(r'\(.*?\)', self.tweet)
            except:
                return "could not extract parameters even though the request was formed properly, please inform the devs"
            return res
        else:
            return self.help_message





if __name__ == "__main__":
    pass



