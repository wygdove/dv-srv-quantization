# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 01:22'



from utils import dvtest
from modules import AssetRecord



if __name__=='__main__':
    assetRecord={
        "recordDate":"2019-08-22 13:30:57",
        "recordInOut":"1000",
        "recordHolding":"0",
        "accountCode":"UA000031",
    }
    # AssetRecord.saveAssetRecord(assetRecord)


    assetRecord={
        "recordCode":"AR000000000002",
        "recordDate":"2019-08-22 13:30:57",
        "recordInOut":"10000000",
        "recordHolding":"0",
        "accountCode":"UA000031",
    }
    # AssetRecord.saveAssetRecord(assetRecord)

    # AssetRecord.deleteAssetRecord({"recordCode":"AR000000000001"})


    res=AssetRecord.getAssetRecords()
    dvtest.tprint(res)

