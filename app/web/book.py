# -*- coding: UTF-8 -*-

# Description: 存放视图函数
#      Author: Mario
#    Datetime: 2019-09-23 08:09
from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook

web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    if isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
