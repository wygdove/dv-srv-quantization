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
    SEQUENCES={
        "ItemTest":"SeqItemTest",  # 测试
        "UserAccount":"SeqUserAccount",  # 账户
        "AssetRecord":"SeqAssetRecord",  # 资产记录
        "Transaction":"SeqTransaction",  # 交易
        "InvestClass":"SeqInvestClass",  # 投资类别
        "Investment":"SeqInvestment",  # 投资标的
        "":"",
    }



class ProdConfig(Config):
    DEBUG=False


class DevConfig(Config):
    DEBUG=True

