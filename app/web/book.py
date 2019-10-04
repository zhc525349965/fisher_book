# -*- coding: UTF-8 -*-

# Description: 存放book视图函数
#      Author: Mario
#    Datetime: 2019-09-23 08:09
import json

from flask import jsonify, request, render_template

from app.forms.book import SearchForm
from app.view_models.book import BookCollection
from app.web.create_blueprint import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    yushu_book = YuShuBook()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        if isbn_or_key == 'key':
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    return jsonify(form.errors)


@web.route('/test')
def test():
    r = {
        'name': 'Mario',
        'age': 18
    }
    return render_template('test.html', data=r)
