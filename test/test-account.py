# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 10:34'


from utils import dvtest
from modules import account



if __name__=='__main__':
    res=account.getUserAccount()
    dvtest.tprint(res)


