# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 01:21'


from config import config
from utils import dvcomn,dvdate,dvajax
from component import dvuser,dvmongo,dvseq

module_flag="AssetRecord"


def init():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[module_flag])
    return coll


def getAssetRecords():
    coll=init()
    query={}
    res=dvmongo.find(coll,query)
    return dvajax.success(res)


def saveAssetRecord(assetRecord):
    coll=init()
    '''
    assetRecord={
        "isIntoSummary":"",
        "currency":"",
        "accountCode":"",
    }
    '''
    if dvcomn.hasKeyStr(assetRecord,"accountCode"):
        query={"accountCode":assetRecord["accountCode"]}
    else:
        query=None
        assetRecord["accountCode"]=dvseq.getNextCode(module_flag,"UA",6)
        assetRecord["createUser"]=dvuser.getCurrentUser()
        assetRecord["createTime"]=dvdate.getNow()
    assetRecord["updateUser"]=dvuser.getCurrentUser()
    assetRecord["updateTime"]=dvdate.getNow()
    res=dvmongo.save(coll,query,assetRecord)
    return dvajax.success(res)

def deleteAssetRecord(assetRecord):
    coll=init()
    res=-1
    # print assetRecord
    # print assetRecord["accountCode"]
    # print dvcomn.hasKeyStr(assetRecord,"accountCode")
    if dvcomn.hasKeyStr(assetRecord,"accountCode"):
        res=dvmongo.deleteOneByCode(coll,{"accountCode":assetRecord["accountCode"]})
    else: return dvajax.norequest()
    if res==1: return dvajax.success(res)
    else: return dvajax.error('删除失败',res)

