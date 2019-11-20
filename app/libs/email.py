# -*- coding: UTF-8 -*-

# Description: 发送邮件
#      Author: Mario
#    Datetime: 2019-11-20 09:08
from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_mail(to, subject, template, **kwargs):
    msg = Message('[鱼书] ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)

    mail.send(msg)
    pass
