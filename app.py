# coding=utf-8
__author__='wygdove'
__time__='2020/1/5 22:39'


from flask import Flask,request
import config
from component import dvuser

from modules import *



appname="dv-src-quantization"
app=Flask(appname)
app.config.from_object(config.DevConfig)





@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/test",methods=['POST'])
def test():
    param=request.form['param']
    return param






# app.add_url_rule("/account/getUserAccount","/account/getUserAccount",account.getUserAccount)
@app.route("/account/getUserAccount",methods=['POST'])
# @app.route("/account/getUserAccount")
def getUserAccount():
    param=request.json
    param["createUser"]=dvuser.getCurrentUser()
    return UserAccount.getUserAccount()

@app.route("/account/saveUserAccount",methods=['POST'])
def saveUserAccount():
    param=request.json
    return UserAccount.saveUserAccount(param)

@app.route("/account/deleteUserAccount",methods=['POST'])
def deleteUserAccount():
    param=request.json
    return UserAccount.deleteUserAccount(param)









if __name__=='__main__':
    host='127.0.0.1'
    # host='0.0.0.0'
    port=8010
    debugMode=True
    app.run(host,port,debugMode)
