# -*- coding: UTF-8 -*-

# Description: 发送邮件
#      Author: Mario
#    Datetime: 2019-11-20 09:08
from flask_mail import Message

from app import mail


def send_mail(to, subject, template):
    msg = Message('测试邮件', sender='525349965@qq.com', body='Test', recipients=['hongchen.zhang@ninebot.com'])
    mail.send(msg)
    pass
