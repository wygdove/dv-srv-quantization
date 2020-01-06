# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 15:29'


from config import config
from utils import dvmongo
from utils import dvajax




def getUserAccount():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,"classCollt")
    query={}
    res=dvmongo.find(coll,query)
    return dvajax.success(res)