"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.forms.auth import RegisterForm, LoginFrom, EmailForm
from app.models.base import db
from app.models.user import User
from app.web.create_blueprint import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_url = request.args.get('next')
            if not next or not next_url or not next_url.startswith('/'):
                next_url = url_for('web.index')
            return redirect(next_url)
        else:
            flash('账号或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            from app.libs.email import send_mail
            send_mail(form.email.data, '重置你的密码', 'email/reset_password.html', user=user, token='123123')
    return render_template('auth/forget_password_request.html', form=form)


# 单元测试
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
