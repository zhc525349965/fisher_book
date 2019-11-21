# -*- coding: UTF-8 -*-

# Description: 注册流程的数据校验
#      Author: Mario
#    Datetime: 2019-10-05 12:41
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from app.models.user import User


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])


class LoginFrom(EmailForm):
    password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32, message='密码长度为6-32位')])


class RegisterForm(LoginFrom):
    # email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    # password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32, message='密码长度为6-32位')])
    nickname = StringField(validators=[DataRequired(message='请输入昵称'), Length(2, 10, message='昵称最少2个字符，最长10个字符')])

    @staticmethod
    def validate_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message='电子邮件已被注册')

    @staticmethod
    def validate_nickname(field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError(message='昵称已被注册')


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[DataRequired(), Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
                                          EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[DataRequired(), Length(6, 32)])
