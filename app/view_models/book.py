# -*- coding: UTF-8 -*-

# Description: book的视图类(主要用于页面渲染时候的信息整理)
#      Author: Mario
#    Datetime: 2019-10-04 11:05


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    """
    历史遗留问题，重构代码后保留之前的思路
    """

    @classmethod
    def package_single(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = 1
            result['books'] = [cls.__cut_book_data(data)]
        return result

    @classmethod
    def package_collection(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            result['total'] = data['total']
            result['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return result

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
