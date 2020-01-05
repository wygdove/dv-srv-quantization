from flask import Flask,request

appname="dv-src-quantization"
app=Flask(appname)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/test",methods=['POST'])
def test():
    param=request.form['param']
    return param


if __name__=='__main__':
    app.run('127.0.0.1',8010,True)
