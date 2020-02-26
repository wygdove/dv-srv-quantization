# coding=utf-8
__author__='wygdove'
__time__='2020/2/27 00:39'



from config import config
from utils import dvcomn,dvdate,dvajax
from component import dvuser,dvmongo,dvseq

module_flag="ItemTest"


def init():
    db=dvmongo.getDb(config.Config.MONGODB_CONF)
    coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[module_flag])
    return coll


def getCurrentDb():
    coll=init()
    fullname=dvmongo.getFullname(coll)
    return dvajax.success(fullname)


