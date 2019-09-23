# -*- coding: UTF-8 -*-

# Description: APP初始化文件
#      Author: Mario
#    Datetime: 2019-09-23 09:17
from flask import Flask
from app.web.book import web


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(web)
