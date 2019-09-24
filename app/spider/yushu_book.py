# -*- coding: UTF-8 -*-

# Description: 存储关于调用书籍接口的类
#      Author: Mario
#    Datetime: 2019-09-23 07:51
from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    base_url = 'http://t.yushu.im/'
    isbn_url = 'v2/book/isbn/{}'
    keyword_url = 'v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = (cls.base_url + cls.isbn_url).format(isbn)
        result = HTTP.get(url=url)

        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = (cls.base_url + cls.keyword_url).format(keyword, current_app.config['PER_PAGE'],
                                                      cls.calculate_start(page))
        result = HTTP.get(url=url)

        return result

    @staticmethod
    def calculate_start(page):
        return current_app.config['PER_PAGE'] * (page - 1)
