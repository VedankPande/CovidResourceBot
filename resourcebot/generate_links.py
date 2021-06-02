""" generate links from given request parameters """
from .database.db_utils import DatabaseHandler
import re

#verified pune (bed OR beds OR icu OR oxygen OR ventilator OR ventilators) -"not verified" -"unverified" -"needed" -"need" -"needs" -"required" -"require" -"requires" -"requirement" -"requirements"
#restrict_list = ['need','needs','needed','require','required','requires','requirement','requirements']

BASE = 'https://twitter.come/search/?q=' #base string for urls
db = r"/home/vedank/Desktop/code/ResourceBot/database.db"
handler = DatabaseHandler(db)
restrict_list = handler.get_all('restrict')

class LinkGen:
    def __init__(self):
        self.BASE = 'https://twitter.com/search/?q='
    
    def generate_link(self,parameters):

        link = 'https://twitter.com/search/?q='

        #Check the param is request or provide
        provide = False
        provide_group = ''
        if parameters[-1][0] == 'provide':
            provide = True
        
        for idx,subparam in enumerate(parameters):
            #cities
            if idx == 0:
                for param in subparam:
                    link += f"{param} "
                    
            #search queries
            if idx == 1:
                group = self.get_group(subparam) #add resource words

                if provide:
                    provide_group += self.get_group(restrict_list) #add provide words

                if not provide:
                    group += " verified available"

                else:
                    group += " " + provide_group + " "
                link += f"{group}"

            #negate queries
            if idx == 2 and subparam[0]!='provide': #make sure 3rd param isn't the provide flag (if negate params aren't given)
                negation = self.get_negate(subparam) #negate custom words
                link += negation

        #negate if request
        if not provide:
            negation = self.get_negate(restrict_list)#negate need/require words
            link += negation
        
        #direct to 'latest' tab
        link += "&f=live"
        link = re.sub(' ','+',link)
        print(link)
        return link

    def get_group(self,tokens):
        group = "("
        for token in tokens:
            group += f"{token} OR "
        group = group[:-4]+")" #remove final trailing OR substring
        return group

    def get_negate(self,tokens):
        negate = ''
        for token in tokens:
            negate += f" -{token}"
        return negate

