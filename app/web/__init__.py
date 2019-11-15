# -*- coding: UTF-8 -*-

# Description: 导入视图文件，不导入会导致视图函数不会注册
#      Author: Mario
#    Datetime: 2019-09-23 09:21
from flask import render_template

from app.web.create_blueprint import web


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html')


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
