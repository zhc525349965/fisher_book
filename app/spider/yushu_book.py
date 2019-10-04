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

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = (self.base_url + self.isbn_url).format(isbn)
        result = HTTP.get(url=url)
        self.__fill_single(result)
        return result

    def search_by_keyword(self, keyword, page=1):
        url = (self.base_url + self.keyword_url).format(keyword, current_app.config['PER_PAGE'],
                                                        self.calculate_start(page))
        result = HTTP.get(url=url)
        self.__fill_collection(result)
        return result

    def calculate_start(self, page):
        return current_app.config['PER_PAGE'] * (page - 1)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
