# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 13:56'


from utils import dvtest
from component import dvseq


def getNextId():
    seqName="UserAccount"
    seqName="Transaction"
    dvtest.tprint(dvseq.getNextId(seqName))

def getNextCode():
    seqName="InvestClass"
    # seqName="Transaction"
    dvtest.tprint(dvseq.getNextCode(seqName,"UA",5))


def deleteSequence():
    seqName="InvestClass"
    dvtest.tprint(dvseq.deleteSequence(seqName))


if __name__ == '__main__':
    # getNextId()
    # getNextCode()
    deleteSequence()
