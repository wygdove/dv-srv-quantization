# coding=utf-8
__author__='wygdove'
__time__='2020/3/22 18:07'



from config import config
from component import dvmongo
from utils import dvtest
import json


moduleFlag='Transaction'
db=dvmongo.getDb(config.Config.MONGODB_CONF)
coll=dvmongo.getCollByDb(db,config.Config.MONGODB_BUCKETS[moduleFlag])


data='''
'''


if __name__ == '__main__':
    jdata=json.loads(data)
    result=jdata['result']
    for item in result:
        id=item['_id']['$oid']
        dvmongo.deleteById(coll,id)


