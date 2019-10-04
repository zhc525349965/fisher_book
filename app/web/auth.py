"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from app.web.create_blueprint import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


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
