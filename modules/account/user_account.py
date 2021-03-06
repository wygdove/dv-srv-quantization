# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 15:29'


from config import config
from utils import dvcomn,dvdate,dvajax
from component import dvuser,dvmongo,dvseq

module_flag="UserAccount"


def init():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[module_flag])
    return coll


def getUserAccount():
    coll=init()
    query={}
    res=dvmongo.find(coll,query)
    return dvajax.success(res)


def saveUserAccount(userAccount):
    coll=init()
    '''
    userAccount={
        "accountName":"",
        "isIntoSummary":"",
        "currency":""
    }
    '''
    if dvcomn.hasKeyStr(userAccount,"accountCode"):
        query={"accountCode":userAccount["accountCode"]}
    else:
        query=None
        userAccount["accountCode"]=dvseq.getNextCode(module_flag,"UA",6)
        userAccount["createUser"]=dvuser.getCurrentUser()
        userAccount["createTime"]=dvdate.getNow()
    userAccount["updateUser"]=dvuser.getCurrentUser()
    userAccount["updateTime"]=dvdate.getNow()
    res=dvmongo.save(coll,query,userAccount)
    return dvajax.success(res)

def deleteUserAccount(userAccount):
    coll=init()
    res=-1
    # print userAccount
    # print userAccount["accountCode"]
    # print dvcomn.hasKeyStr(userAccount,"accountCode")
    if dvcomn.hasKeyStr(userAccount,"accountCode"):
        res=dvmongo.deleteOneByCode(coll,{"accountCode":userAccount["accountCode"]})
    else: return dvajax.norequest()
    if res==1: return dvajax.success(res)
    else: return dvajax.error('删除失败',res)

