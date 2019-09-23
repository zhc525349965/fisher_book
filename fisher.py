# -*- coding: UTF-8 -*-

# Description: 入口文件
#      Author: Mario
#    Datetime: 2019-09-22 12:34

from flask import Flask, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    if isbn_or_key == 'key':
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
