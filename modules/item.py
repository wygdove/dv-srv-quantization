# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 19:00'



from config import config
from utils import dvcomn,dvdate,dvajax
from component import dvuser,dvmongo,dvseq





def init(itemConfig):
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[itemConfig["moduleFlag"]])
    return coll


def getItems(itemConfig,itemData):
    coll=init(itemConfig)
    query=itemData
    res=""
    if itemConfig.has_key("sortField") and not dvcomn.isNullStr(itemConfig["sortField"]):
        sortField=itemConfig["sortField"]
        sortType=itemConfig["sortType"] if itemConfig.has_key("sortType") else ''
        res=dvmongo.findSort(coll,query,sortField,sortType)
    else:
        res=dvmongo.find(coll,query)
    return dvajax.success(res)


def saveItem(itemConfig,itemData):
    coll=init(itemConfig)
    if dvcomn.hasKeyStr(itemData,itemConfig["codeKey"]):
        query={itemConfig["codeKey"]:itemData[itemConfig["codeKey"]]}
    else:
        query=None
        itemData[itemConfig["codeKey"]]=dvseq.getNextCode(itemConfig["moduleFlag"],itemConfig["codePrefix"],itemConfig["codeLength"])
        itemData["createUser"]=dvuser.getCurrentUser()
        itemData["createTime"]=dvdate.getNow()
    itemData["updateUser"]=dvuser.getCurrentUser()
    itemData["updateTime"]=dvdate.getNow()
    res=dvmongo.save(coll,query,itemData)
    return dvajax.success(res)


def deleteItem(itemConfig,itemData):
    coll=init(itemConfig)
    res=-1
    if dvcomn.hasKeyStr(itemData,itemConfig["codeKey"]):
        res=dvmongo.deleteOneByCode(coll,{itemConfig["codeKey"]:itemData[itemConfig["codeKey"]]})
    else: return dvajax.norequest()
    if res==1: return dvajax.success(res)
    else: return dvajax.error('删除失败',res)

