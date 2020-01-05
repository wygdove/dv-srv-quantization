from flask import Flask

app=Flask("dv-srv-quantization")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__=='__main__':
    app.run()
