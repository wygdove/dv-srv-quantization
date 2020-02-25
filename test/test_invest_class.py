# coding=utf-8
__author__='wygdove'
__time__='2020/2/25 18:02'



from utils import dvtest
from modules import item



if __name__=='__main__':
    itemConfig={
        "moduleFlag":"InvestClass",
        "codeKey":"InvestClassIdCode",
        "codePrefix":"IC",
        "codeLength":6,
    }


    itemData={
        # "investClassIdCode":"",
        "investClassCode":"IndiceFund",
        "investClassName":"指数基金",
    }
    # item.saveItem(itemConfig,itemData)

    # item.deleteItem(itemConfig,{itemConfig["codeKey"]:"IC000007"})


    itemDatas=[
        {"investClassCode":"IndiceFund","investClassName":"指数基金"},
        {"investClassCode":"ConvertibleBond","investClassName":"可转债"},
        {"investClassCode":"Stock","investClassName":"股票"},
        {"investClassCode":"StockFund","investClassName":"股票基金"},
        {"investClassCode":"Bond","investClassName":"债券"},
        {"investClassCode":"MoneyFund","investClassName":"货币基金"},
        {"investClassCode":"FinancialProduct","investClassName":"理财产品"}
    ]
    # for id in itemDatas:
    #     item.saveItem(itemConfig,id)


    res=item.getItems(itemConfig,itemData)
    dvtest.tprint(res)

