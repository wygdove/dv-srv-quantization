# coding=utf-8
__author__='wygdove'
__time__='2020/2/25 18:02'




from utils import dvtest
from modules import item



if __name__=='__main__':
    itemConfig={
        "moduleFlag":"Investment",
        "codeKey":"investmentIdCode",
        "codePrefix":"IV",
        "codeLength":6,
    }

    itemData={
        # "investmentIdCode":"",
        "investmentCode":"510500",
        "investmentName":"500ETF",
        "investClassCode":"IndiceFund",
        "investClassName":"指数基金",
    }
    item.saveItem(itemConfig,itemData)

    # item.deleteItem(itemConfig,{itemConfig["codeKey"]:"AR000000000003"})


    res=item.getItems(itemConfig)
    dvtest.tprint(res)



