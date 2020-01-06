# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 15:20'


import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId



def getDb(conf):
    conn=pymongo.MongoClient('mongodb://'+conf["mongoServer"])
    db=conn.get_database(conf["database"])
    # db.authenticate(conf["userName"],conf["password"])
    return db
    
def getCollByDb(db,bucket):
    coll=db.get_collection(bucket)
    return coll

def getColl(conf):
    conn=pymongo.MongoClient('mongodb://'+conf["mongoServer"])
    db=conn.get_database(conf["database"])
    # db.authenticate(conf["userName"],conf["password"])
    coll=db.get_collection(conf["bucket"])
    return coll

def getFullname(coll):
    return coll.full_name



def find(coll,query):
    return findMany(coll,query)

def findOne(coll,query):
    data=coll.find_one(query)
    data=json.loads(dumps(data))
    # return json.dumps(data)
    return data

def findMany(coll,query):
    data=coll.find(query)
    data=json.loads(dumps(data))
    # return json.dumps(data)
    return data

def findById(coll,id):
    data=coll.find({"_id":ObjectId(id)})
    data=json.loads(dumps(data))
    # return json.dumps(data)
    return data



def insert(coll,data):
    return coll.insert(data)

def delete_many(coll,query):
    coll.delete_many(query)



