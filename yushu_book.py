# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-09-23 07:51
from httper import HTTP


class YuShuBook:
    base_url = 'http://t.yushu.im/'
    isbn_url = 'v2/book/isbn/{}'
    keyword_url = 'v2/book/search?q={}&count={}start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = (cls.base_url + cls.isbn_url).format(isbn)
        result = HTTP.get(url=url)

        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = (cls.base_url + cls.keyword_url).format(keyword, count, start)
        result = HTTP.get(url=url)

        return result
