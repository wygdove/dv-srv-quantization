# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 14:49'



class Config(object):
    MONGODB_CONF={
        "mongoServer":"127.0.0.1:37017",
        "database":"quantizationdev",
        "userName":"quantization",
        "password":""
    }
    MONGODB_BUCKETS={
        "Sequence":"Sequence",
        "ItemTest":"ItemTest",
        "UserAccount":"UserAccount",
        "AssetRecord":"AssetRecord",
        "Transaction":"Transaction",
        "InvestClass":"InvestClass",
        "Investment":"Investment",
    }



class ProdConfig(Config):
    DEBUG=False


class DevConfig(Config):
    DEBUG=True

