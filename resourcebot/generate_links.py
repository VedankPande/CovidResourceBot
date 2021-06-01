""" generate links from given request parameters """
from typing import Tuple
from urllib.parse import quote

#verified pune (bed OR beds OR icu OR oxygen OR ventilator OR ventilators) -"not verified" -"unverified" -"needed" -"need" -"needs" -"required" -"require" -"requires" -"requirement" -"requirements"

BASE = 'https://twitter.come/search/?q=' #base string for urls
restrict_list = ['need','needs','needed','require','required','requires','requirement','requirements']

class LinkGen:
    def __init__(self):
        self.BASE = 'https://twitter.com/search/?q='
    
    def generate_link(self,parameters):
        provide = False
        provide_group = ''
        if parameters[-1][0] == 'provide':
            provide = True
        link = 'https://twitter.com/search/?q='
        for idx,subparam in enumerate(parameters):
            if idx == 0:
                for param in subparam:
                    link += f"{param} "
            if idx == 1:
                group = "("
                for param in subparam:
                    group += f"{param} OR "
                group = group[:-4] + ")"
                if provide:
                    provide_group += '('
                    for restrict in restrict_list:
                        provide_group += f"{restrict} OR "
                    provide_group = provide_group[:-4]
                    provide_group += ')'
                    print(provide_group)
                if not provide:
                    group += " verified available"
                else:
                    group += " " + provide_group + " "

                link += f"{group}"
            if idx == 2 and subparam[0]!='provide': #make sure 3rd param isn't the provide flag (if negate params aren't given)
                for param in subparam:
                    link += f" -\"{param}\""
        if not provide:
            for restrict in restrict_list:
                link += f" -\"{restrict}\""

        return link + "&f=live"


