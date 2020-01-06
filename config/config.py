# coding=utf-8
__author__='wygdove'
__time__='2020/1/6 14:49'



class Config(object):
    MONGODB_CONF={"mongoServer":"127.0.0.1:37017","database":"quantization","userName":"quantization","password":"okmPL<","bucket":"classCollt"}

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
