"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.web.create_blueprint import web
from flask_login import login_required


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
