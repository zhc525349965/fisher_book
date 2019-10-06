# -*- coding: UTF-8 -*-

# Description: 注册流程的数据校验
#      Author: Mario
#    Datetime: 2019-10-05 12:41
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class LoginFrom(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32, message='密码长度为6-32位')])


class RegisterForm(LoginFrom):
    # email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    # password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32, message='密码长度为6-32位')])
    nickname = StringField(validators=[DataRequired(message='请输入昵称'), Length(2, 10, message='昵称最少2个字符，最长10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message='电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError(message='昵称已被注册')
