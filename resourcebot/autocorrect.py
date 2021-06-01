import Levenshtein

#TODO: convert lists to dictionaries and add alternative words for each word in it's values
cities = ['pune','mumbai','banglore','kochi','delhi','kolkatta','madras','ahmedabad','jaipur','nagpur','thane'] #poona
resources = ['oxygen','ventilator','bed','icu','test','fabiflu','remdesivir','favipiravir','tocilizumab','plasma','food','ambulance','amphotericin B']
resource_dict = {'oxygen':[],'ventilator':['ventilators'],'bed':['beds'],'icu':[],'test':['tests','testing'],'fabiflu' :['fabiflu'],'remdesivir':['remdesivir'],'favipiravir':['favepiravir'],'tocilizumab':['tocilizumab'],'plasma':['plasma'],'food':['foods'],'ambulance':['amblances'],'amphotericin B' :['amphotericin B']}

# corrects for spelling errors
def correct(parameters):
    res = parameters.copy()
    for p_idx,params in enumerate(parameters):
        if p_idx == 0:
            for idx,param in enumerate(params):
                res[0][idx] = find_match(param,"cities")[0]
        if p_idx == 1:
            for idx,param in enumerate(params):
                res[1][idx] = find_match(param,"resources")[0]
    
    return res
                
# util function to find match for input word
def find_match(request,lookup):
    if lookup == "cities":
        return min([[cities[idx],Levenshtein.distance(request,entry)] for idx,entry in enumerate(cities)],key= lambda x: x[1])

    elif lookup == "resources":
        return min([[resources[idx],Levenshtein.distance(request,entry)] for idx,entry in enumerate(resources)],key = lambda x: x[1])  
    
    else:
        return None

# adds alternative words if available in the params
def add_alternatives(request):
    res = request.copy()
    for resource in request:
        if resource in resource_dict.keys():
            for alt in resource_dict[resource]:
                res.append(alt)
    return res

# wraps functions together
def tune(parameters):
    res = correct(parameters)
    res[1] = add_alternatives(res[1])
    return res


    




if __name__ == "__main__":
    pass
