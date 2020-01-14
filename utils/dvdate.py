# coding=utf-8
__author__='wygdove'
__time__='2020/1/14 11:20'


import time



def getNow():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def getToday():
    return time.strftime("%Y-%m-%d",time.localtime())





