# -*- coding: UTF-8 -*-

# Description: book视图的验证文件
#      Author: Mario
#    Datetime: 2019-09-24 08:27
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
