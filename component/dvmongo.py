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



def insert(coll,data):
    return coll.insert(data)

def update(coll,query,data):
    return coll.update(query,{"$set":data})

def updateById(coll,id,data):
    return coll.update({"_id":ObjectId(id)},{"$set":data})

def updateOne(coll,query,data):
    return coll.update_one(query,{"$set":data})

def updateOneById(coll,id,data):
    return coll.update_one({"_id":ObjectId(id)},{"$set":data})

def delete_many(coll,query):
    return coll.delete_many(query)



def save(coll,query,data):
    result=0
    if query==None: res=None
    else: res=find(coll,query)
    if res==None or len(res)==0:
        insert(coll,data)
        result=1
    elif len(res)==1:
        resdata=res[0]
        mongoid=resdata["_id"]["$oid"]
        del resdata["_id"]
        resdata.update(data)
        updateOneById(coll,mongoid,resdata)
        result=1
    else:
        result=len(res)
    return result

def delete(coll,query):
    return coll.delete_many(query)

def deleteById(coll,id):
    return coll.delete_many({"_id":ObjectId(id)})

def deleteOneByCode(coll,query):
    result=0
    if query==None: res=None
    else: res=find(coll,query)
    if res==None or len(res)==0:
        result=0
    elif len(res)==1:
        coll.delete_many(query)
        result=1
    else:
        result=len(res)
    return result






def loadData(data):
    # return json.dumps(data)
    return json.loads(dumps(data))


def find(coll,query):
    return findMany(coll,query)

def findMany(coll,query):
    data=coll.find(query)
    return loadData(data)

def findOne(coll,query):
    data=coll.find_one(query)
    return loadData(data)

def findById(coll,id):
    data=coll.find({"_id":ObjectId(id)})
    data=json.loads(dumps(data))
    return loadData(data)


def findSort(coll,query,sortField,sortType):
    return findManySort(coll,query,sortField,sortType)

def findManySort(coll,query,sortField,sortType):
    sortType=pymongo.DESCENDING if 'desc'==sortType else pymongo.ASCENDING
    data=coll.find(query).sort(sortField,sortType)
    return loadData(data)


def distinct(coll,field,query):
    data=coll.distinct(field,query)
    return data



