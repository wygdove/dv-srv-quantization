# coding=utf-8
__author__='wygdove'
__time__='2020/1/5 22:39'


from flask import Flask,request
import config
from component import dvuser

from modules import item



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






@app.route("/common/getItem",methods=['POST'])
def getItem():
    param=request.json
    param["itemData"]["createUser"]=dvuser.getCurrentUser()
    return item.getItems(param["itemConfig"],param["itemData"])

@app.route("/common/saveItem",methods=['POST'])
def saveItem():
    param=request.json
    return item.saveItem(param["itemConfig"],param["itemData"])

@app.route("/common/deleteItem",methods=['POST'])
def deleteItem():
    param=request.json
    return item.deleteItem(param["itemConfig"],param["itemData"])








if __name__=='__main__':
    host='127.0.0.1'
    # host='0.0.0.0'
    port=8010
    debugMode=True
    app.run(host,port,debugMode)
