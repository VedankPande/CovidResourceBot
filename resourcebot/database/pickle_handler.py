import pickle

def load_data():
    dbfile = open('/home/vedank/Desktop/code/ResourceBot/resource.pickle','rb')
    db = pickle.load(dbfile)
    return db

if __name__ == "__main__":
    pass