# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 19:00'



from utils import dvtest
from modules import item



if __name__=='__main__':
    itemConfig={
        "moduleFlag":"AssetRecord",
        "codeKey":"recordCode",
        "codePrefix":"AR",
        "codeLength":12,
    }

    itemData={
        # "recordCode":"",
        "recordDate":"2019-08-22 13:32:12",
        "recordInOut":"100",
        "recordHolding":"0",
        "accountCode":"UA000031",
    }
    # item.saveItem(itemConfig,itemData)

    item.deleteItem(itemConfig,{itemConfig["codeKey"]:"AR000000000003"})


    res=item.getItems(itemConfig)
    dvtest.tprint(res)

