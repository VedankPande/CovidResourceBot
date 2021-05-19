import resourcebot
from .validation_utils import valUtils


cities = ['pune','mumbai','banglore','kochi','delhi','kolkatta','madras','ahmedabad','jaipur','nagpur','thane']
resources = ['oxygen','ventilator','bed','icu','test','fabiflu','remdesivir','favipiravir','tocilizumab','plasma','food','ambulance','amphotericin B']

def find_match(request,lookup):
    if lookup == "cities":
        return min([[cities[idx],valUtils.get_distance(request,entry)] for idx,entry in enumerate(cities)],key= lambda x: x[1])

    elif lookup == "resources":
        return min([[resources[idx],valUtils.get_distance(request,entry)] for idx,entry in enumerate(resources)],key = lambda x: x[1])  




if __name__ == "__main__":
    pass
