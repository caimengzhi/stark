#!/usr/bin/python
# _*_ coding: utf-8 _*_

from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return '<h1>Hello caimengzhi </h1>'


@app.route('/test/<path:name>/', methods=['GET', 'POST'])
def test(name):
    return str(name)


if __name__ == '__main__':
    app.run()
