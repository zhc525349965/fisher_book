# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-10-05 11:44
from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

    # 用于对应user模型，指定这本书是那个用户赠予
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))

    # 关联书籍isbn
    # 字符串类型，长度15 不可为空
    isbn = Column(String(15), nullable=False)
