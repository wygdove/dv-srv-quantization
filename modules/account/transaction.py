# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 00:58'



from config import config
from utils import dvcomn,dvdate,dvajax
from component import dvuser,dvmongo,dvseq

module_flag="Transaction"


def init():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[module_flag])
    return coll


def getTransactions():
    coll=init()
    query={}
    res=dvmongo.find(coll,query)
    return dvajax.success(res)


def saveTransaction(transaction):
    coll=init()
    '''
    transaction={
        "isIntoSummary":"",
        "currency":"",
        "accountCode":"",
    }
    '''
    if dvcomn.hasKeyStr(transaction,"accountCode"):
        query={"accountCode":transaction["accountCode"]}
    else:
        query=None
        transaction["accountCode"]=dvseq.getNextCode(module_flag,"UA",6)
        transaction["createUser"]=dvuser.getCurrentUser()
        transaction["createTime"]=dvdate.getNow()
    transaction["updateUser"]=dvuser.getCurrentUser()
    transaction["updateTime"]=dvdate.getNow()
    res=dvmongo.save(coll,query,transaction)
    return dvajax.success(res)

def deleteTransaction(transaction):
    coll=init()
    res=-1
    # print transaction
    # print transaction["accountCode"]
    # print dvcomn.hasKeyStr(transaction,"accountCode")
    if dvcomn.hasKeyStr(transaction,"accountCode"):
        res=dvmongo.deleteOneByCode(coll,{"accountCode":transaction["accountCode"]})
    else: return dvajax.norequest()
    if res==1: return dvajax.success(res)
    else: return dvajax.error('删除失败',res)

