# coding=utf-8
__author__='wygdove'
__time__='2020/1/22 00:59'


from utils import dvtest
from modules import Transaction



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
        "investmentHolding":0,
        "investmentEarnHistory":0,
        "investmentBuysell":-1,
        "remark":"",
        "accountCode":"UA000031"
    }

    dvtest.tprint(Transaction.getHoldingInvestment())

