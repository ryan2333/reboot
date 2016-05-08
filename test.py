#!/usr/bin/env python
#_*_coding:utf-8_*_

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()