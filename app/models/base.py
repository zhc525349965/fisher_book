# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-10-05 11:44

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # 创建时间， Coloum后面指定在数据中的字段名称
    create_time = Column('create_time', Integer)
    # 状态字段， 1为正常
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
