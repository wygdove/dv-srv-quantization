# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 01:22'



from utils import dvtest
from modules import account



if __name__=='__main__':
    assetRecord={
        "accountName":"货基",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    account.saveAssetRecord(assetRecord)


    assetRecord={
        "accountCode":"UA000024",
        "accountName":"货基222",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    # account.saveAssetRecord(assetRecord)


    res=account.getAssetRecord()
    dvtest.tprint(res)

