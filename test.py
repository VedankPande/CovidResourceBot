""" test code here """ 


def generate_link(parameters):
    link = 'https://twitter.com/search/?q='
    for idx,subparam in enumerate(parameters):
        if idx == 0:
            for param in subparam:
                link = link + f"{param} "
        if idx == 1:
            group = "("
            for param in subparam:
                group = group + f"{param} OR "
            group = group + ")"
            link = link + f"{group}"
        if idx == 2:
            for param in subparam:
                link = link + f" -\"{param}\""
    
    return link + "&f=live"


if __name__ == "__main__":
    params = [['pune'],['oxygen','bed'],['not verified','needs','needed','required']]
    print(generate_link(params))

