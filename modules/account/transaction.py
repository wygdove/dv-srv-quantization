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


def getHoldingInvestment():
    coll=init()
    field="investmentCode"
    query={"investmentHolding":{"$ne":0}}
    res=dvmongo.distinct(coll,field,query)
    return dvajax.success(res)
