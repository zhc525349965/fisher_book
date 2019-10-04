# -*- coding: UTF-8 -*-

# Description: 存放book视图函数
#      Author: Mario
#    Datetime: 2019-09-23 08:09

from flask import request, render_template, flash

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
        # return json.dumps(books, default=lambda o: o.__dict__)

    else:
        # 用消息闪现将提示输出到页面上，取代之前的jsonify
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    # 将视图函数的返回放到最外面，解决validate没有验证通过时没有返回的问题
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail():
    pass

@web.route('/test')
def test():
    r = {
        'name': 'Mario',
        'age': 18
    }
    flash('Hello,Mario', category='test')
    return render_template('test.html', data=r)
