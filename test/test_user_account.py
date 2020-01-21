# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 10:34'


from utils import dvtest
from modules import account



if __name__=='__main__':
    userAccount={
        "accountName":"货基",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    # account.saveUserAccount(userAccount)


    userAccount={
        "accountCode":"UA000024",
        "accountName":"货基222",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    # account.saveUserAccount(userAccount)


    res=account.getUserAccount()
    dvtest.tprint(res)


