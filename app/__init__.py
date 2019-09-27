# -*- coding: UTF-8 -*-

# Description: APP初始化文件
#      Author: Mario
#    Datetime: 2019-09-23 09:17
from flask import Flask

from app.models.book import db
from app.web.book import web


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 将sql alchemy对象注册到APP实例上
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    app.register_blueprint(web)
