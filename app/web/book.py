# -*- coding: UTF-8 -*-

# Description: 存放book视图函数
#      Author: Mario
#    Datetime: 2019-09-23 08:09
from flask import jsonify, request

from app.forms.book import SearchForm
from app.web.create_blueprint import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        result = None

        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_keyword(q)

        return jsonify(result)
    return jsonify(form.errors)
