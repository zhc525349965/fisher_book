"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from flask import current_app

from app.models.base import db
from app.models.gift import Gift
from app.web.create_blueprint import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
