# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-10-05 11:43
from app.models.base import db
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(db.Model):
    # 整数类型 主键
    id = Column(Integer, primary_key=True)
    # 字符串类型，长度24 不可以为空
    nickname = Column(String(24), nullable=False)
    # 字符串类型，长度18 unique指定不可重复，独一无二
    phone_number = Column(String(18), unique=True)
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
