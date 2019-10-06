"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.web.create_blueprint import web


@web.route('/')
def index():
    return 'index'


@web.route('/personal')
def personal_center():
    pass
