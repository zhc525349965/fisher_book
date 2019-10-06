"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.forms.auth import RegisterForm, LoginFrom
from app.models.base import db
from app.models.user import User
from app.web.create_blueprint import web
from flask import render_template, request, redirect, url_for, flash


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.fliter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            pass
        else:
            flash('账号或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


# 单元测试
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass