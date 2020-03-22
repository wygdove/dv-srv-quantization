# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 13:35'


from config import config
from component import dvmongo


bucket_flag="Sequence"


def init():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[bucket_flag])
    return coll


def getNextId(seqName):
    nextid=0
    coll=init()
    seqName=config.Config.SEQUENCES[seqName]
    query={"sequenceName":seqName}
    res=dvmongo.find(coll,query)
    if res==None or len(res)==0:
        seqdata={
            "sequenceName":seqName,
            "startBy":1,
            "increaseBy":1,
            "lastNumber":1
        }
        print dvmongo.insert(coll,seqdata)
        nextid=1
    elif len(res)==1:
        seqdata=res[0]
        nextid=seqdata["lastNumber"]+seqdata["increaseBy"]
        seqdata["lastNumber"]=nextid
        mongoid=seqdata["_id"]["$oid"]
        del seqdata["_id"]
        dvmongo.updateOneById(coll,mongoid,seqdata)
    else:
        nextid=0
    return nextid


def getNextCode(seqName,prefix,length):
    nextcode=prefix
    tempcode=str(getNextId(seqName))
    for i in xrange(0,length-len(tempcode)):
        nextcode+="0"
    nextcode+=tempcode
    return nextcode




def deleteSequence(seqName):
    coll=init()
    seqName=config.Config.SEQUENCES[seqName]
    query={"sequenceName":seqName}
    res=dvmongo.find(coll,query)
    dvmongo.deleteById(coll,res[0]['_id']['$oid'])
    return dvmongo.find(coll,query)

