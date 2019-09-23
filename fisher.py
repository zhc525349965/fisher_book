# -*- coding: UTF-8 -*-

# Description: 入口文件
#      Author: Mario
#    Datetime: 2019-09-22 12:34

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
