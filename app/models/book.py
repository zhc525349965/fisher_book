# -*- coding: UTF-8 -*-

# Description: 书籍的业务模型
#      Author: Mario
#    Datetime: 2019-09-25 07:58
from sqlalchemy import Column, Integer, String, Date


class Book:
    # 整数类型 主键 自增长
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 字符串类型，长度50 不可以为空
    title = Column(String(50), nullable=False)
    # 字符串类型，长度30 默认值'未名'
    author = Column(String(30), default='未名')
    # 字符串类型，长度20
    binding = Column(String(20))
    # 字符串类型，长度50
    publisher = Column(String(50))
    # 字符串类型，长度20
    price = Column(String(20))
    # 整数类型
    pages = Column(Integer)
    # 字符串类型，长度20
    pubdate = Column(String(20))
    # 字符串类型，长度15 不可为空 unique指定不可重复，独一无二
    isbn = Column(String(15), nullable=False, unique=True)
    # 字符串类型
    summary = Column(String(10000))
    # 字符串类型
    image = Column(String(50))
