# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 10:34'


from utils import dvtest
from modules import UserAccount



if __name__=='__main__':
    userAccount={
        "accountName":"货基",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    # UserAccount.saveUserAccount(userAccount)


    userAccount={
        "accountCode":"UA000024",
        "accountName":"货基222",
        "isIntoSummary":"1",
        "currency":"CNY"
    }
    # UserAccount.saveUserAccount(userAccount)


    res=UserAccount.getUserAccount()
    dvtest.tprint(res)


