"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from flask import current_app, flash

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
    if current_user.can_save_to_wish_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经存在于赠送清单或心愿清单，请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
