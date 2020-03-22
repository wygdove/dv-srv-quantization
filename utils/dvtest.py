# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 10:42'



import json


def tprint(object):
    print json.dumps(object,encoding='utf-8',ensure_ascii=False)

def presult(object):
    data=json.dumps(object,encoding='utf-8',ensure_ascii=False)
    result=json.loads(data)['result']
    return json.dumps(result,encoding='utf-8',ensure_ascii=False)

