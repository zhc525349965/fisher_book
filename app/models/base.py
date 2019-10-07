# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-10-05 11:44
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


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
