# -*- coding: UTF-8 -*-

# Description: APP初始化文件
#      Author: Mario
#    Datetime: 2019-09-23 09:17
from flask import Flask
from flask_mail import Mail

from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    # 将sql alchemy对象注册到APP实例上
    db.init_app(app=app)
    with app.app_context():
        db.create_all()

    # 将LoginManager注册到APP实例上
    login_manager.init_app(app=app)
    # 指定登录页面（在未登录时打开需要登录的页面，会自动跳转到该页面）
    login_manager.login_view = 'web.login'
    # 指定跳转到登录页面时flash的消息内容
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
