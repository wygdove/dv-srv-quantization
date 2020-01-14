# coding=utf-8
__author__='wygdove'
__time__='2020/1/14 16:53'



def isNull(obj):
    return obj==None

def isNotNull(obj):
    return not isNull(obj)

def isNullStr(str):
    return str==None or type(str)!=type("") or str==""

def isNotNullStr(str):
    return not isNullStr(str)

def isNullArr(arr):
    return arr==None or type(arr)!=type([]) or len(arr)==0

def isNotNullArr(arr):
    return not isNullArr(arr)




def hasKey(obj,key):
    return obj.has_key(key) and isNotNull(obj[key])

def hasKeyStr(obj,key):
    return obj.has_key(key) and isNotNullStr(obj[key])

def hasKeyArr(obj,key):
    return obj.has_key(key) and isNotNullArr(obj[key])


