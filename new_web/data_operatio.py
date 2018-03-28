import pymongo
from pymongo import MongoClient
import tool


def MClient():
    client = MongoClient('localhost', 27017)
    db = client['mydb2']
    my_set = db['news']
    return my_set


def date_find_one(date):
    my_set = MClient()
    data = my_set.find({'date':date})
    return data


def date_find_all():
    news= []
    time_set = tool.time_set()
    for i in time_set:
        news.append(date_find_one(i))
    return news
