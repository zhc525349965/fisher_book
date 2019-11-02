"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from app.web.create_blueprint import web


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
