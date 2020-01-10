# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 13:56'


from utils import dvtest
from utils import dvseq




def getNextId():
    seqName="UserAccount"
    seqName="Transaction"
    dvtest.tprint(dvseq.getNextId(seqName))

def getNextCode():
    seqName="UserAccount"
    # seqName="Transaction"
    dvtest.tprint(dvseq.getNextCode(seqName,"UA",5))


if __name__ == '__main__':
    # getNextId()
    getNextCode()
