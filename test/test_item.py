# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 19:00'



from utils import dvtest
from modules import item as Item


datas=''''''



if __name__=='__main__':
    itemConfig={
        "moduleFlag":"Transaction",
        "codeKey":"transactionCode",
        "codePrefix":"TR",
        "codeLength":12,
    }
    itemData={
        "transactionCode":"TR000000000012",
        "transactionDate":"2020/02/26 23:30:03",
        "investmentCode":"110063",
        "investmentName":"鹰19转债",
        "investClassCode":"ConvertibleBond",
        "investClassName":"可转债",
        "investmentBuysell":0,
        "investmentEarnHistory":0,
        "investmentHolding":100,
        "remark":"",
        "accountCode":"UA000031",
    }







    # Item.saveItem(itemConfig,itemData)

    # Item.deleteItem(itemConfig,{itemConfig["codeKey"]:"AR000000000119"})
    for i in xrange(3,32):
        break
        # code='AR000000000'+str(i)
        # Item.deleteItem(itemConfig,{itemConfig["codeKey"]:code})

    dataArr=datas.split('\n')
    for data in dataArr:
        break
        da=data.split('\t')
        transactionDate=da[0]
        investmentName=da[1]
        investmentBuysell=float(da[2])
        itemData={
            "transactionDate":transactionDate,
            "investmentCode":'',
            "investmentName":investmentName,
            "investClassCode":'',
            "investClassName":'',
            "investmentBuysell":investmentBuysell,
            "investmentHolding":0,
            "investmentEarnHistory":0,
            "remark":"",
            "accountCode":"UA000031"
        }
        # print itemData
        # Item.saveItem(itemConfig,itemData)

    # dvtest.tprint(Item.getItems(itemConfig,{}))

    dvtest.tprint(Item.getItems({"moduleFlag":"Investment","codeKey":"investmentIdCode"},{}))

