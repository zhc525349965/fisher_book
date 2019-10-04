"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""

from app.web.create_blueprint import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
