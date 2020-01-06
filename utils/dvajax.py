# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 16:11'


resultCode={"success":"000000","error":"999999","user_null":"100001","request_null":"200001","data_null":"800001"}
result={"code":"000000","result":None,"msg":"success","info":""}

def success(obj):
    if obj==None:
        return nodata()
    result["code"]=resultCode["success"]
    result["result"]=obj
    result["msg"]="success"
    result["info"]=""
    return result


def error(msg,info):
    result["code"]=resultCode["error"]
    result["result"]=None
    result["msg"]=msg
    result["info"]=info
    return result






def nouser():
    result["code"]=resultCode["user_null"]
    result["result"]=None
    result["msg"]=""
    result["info"]="user is null"
    return result

def norequest():
    result["code"]=resultCode["request_null"]
    result["result"]=None
    result["msg"]=""
    result["info"]="request is null"
    return result

def nodata():
    result["code"]=resultCode["data_null"]
    result["result"]=None
    result["msg"]=""
    result["info"]="result is null"
    return result





