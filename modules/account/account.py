# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 15:29'


from config import config
from utils import dvdate,dvmongo,dvajax,dvseq,dvuser




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
    if userAccount.has_key("accountCode"):
        query={"accountCode":userAccount["accountCode"]}
    else:
        query={"accountCode":None}
        userAccount["accountCode"]=dvseq.getNextCode(module_flag,"UA",6)
        userAccount["createUser"]=dvuser.getCurrentUser()
        userAccount["createTime"]=dvdate.getNow()
    userAccount["updateUser"]=dvuser.getCurrentUser()
    userAccount["updateTime"]=dvdate.getNow()
    dvmongo.save(coll,query,userAccount)

