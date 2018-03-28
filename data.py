import pymongo
from pymongo import MongoClient

def MClient():
    client = MongoClient('localhost', 27017)
    db = client['mydb2']
    my_set = db['news']
    return my_set

def find_new(url):
    my_set = MClient()
    return bool(my_set.find_one({'url':url}))

def new_insert(new,url,date):
    my_set = MClient()
    news = {
        'new' : new,
        'url' : url,
        'date' : date
    }
    my_set.insert(news)