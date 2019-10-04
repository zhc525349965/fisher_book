"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.web.create_blueprint import web


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
