# -*- coding: UTF-8 -*-

# Description: book视图的验证文件
#      Author: Mario
#    Datetime: 2019-09-24 08:27
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired, Length, Regexp


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField('收件人姓名',
                                 validators=[DataRequired(), Length(min=2, max=20, message='收件人姓名长度必须在2到20个字之间')])
    mobile = StringField('手机号', validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField('留言')
    address = StringField('邮寄地址', validators=[DataRequired(), Length(min=7, max=70, message='地址在7-70个字之间')])
