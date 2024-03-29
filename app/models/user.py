# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-10-05 11:43
from math import floor

from flask import current_app

from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(Base, UserMixin):
    # 整数类型 主键
    id = Column(Integer, primary_key=True)
    # 字符串类型，长度24 不可以为空
    nickname = Column(String(24), nullable=False)
    # 字符串类型，长度18 unique指定不可重复，独一无二
    phone_number = Column(String(18), unique=True)
    # __password属性，在表中字段名称为password, 不能为空
    _password = Column('password', String(128), nullable=False)
    # 字符串类型，长度50 不可重复 不可为空
    email = Column(String(50), unique=True, nullable=False)
    # 布尔行，默认值为false
    confirmed = Column(Boolean, default=False)
    # 浮点型，默认值0
    beans = Column(Float, default=0)
    # 整型 默认值0
    send_counter = Column(Integer, default=0)
    # 整型 默认值0
    receive_counter = Column(Integer, default=0)
    # 字符串类型 长度50
    wx_open_id = Column(String(50))
    # 字符串类型 长度32
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def can_send_drift(self):
        # 每索取两本书，必须送出去一本书
        if self.beans < 1:
            return False
        # 已经送出去的礼物
        success_gifts_count = Gift.query.filter_by(uid=self.id, launched=True).count()
        # 已经索取的礼物
        success_receive_count = Drift.query.filter_by(requester_id=self.id, pending=PendingStatus.Success).count()
        return True if floor(success_receive_count / 2) <= floor(success_gifts_count) else False

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_wish_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @property
    def summary(self):
        return dict(nickname=self.nickname, beans=self.beans, email=self.email,
                    send_receive=str(self.send_counter) + '/' + str(self.receive_counter))

    @staticmethod
    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))
