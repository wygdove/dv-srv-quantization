# coding=utf-8
__author__='wygdove'
__time__='2020/1/10 13:56'


from utils import dvtest
from component import dvseq



# seqName="UserAccount"
seqName="Transaction"


def getNextId():
    dvtest.tprint(dvseq.getNextId(seqName))

def getNextCode():
    dvtest.tprint(dvseq.getNextCode(seqName,"UA",5))


def deleteSequence():
    dvtest.tprint(dvseq.deleteSequence(seqName))


if __name__ == '__main__':
    # getNextId()
    # getNextCode()
    deleteSequence()
