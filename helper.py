# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-09-22 15:10


def is_isbn_or_key(word):
    """
    :param word: 用户传递的关键字
    :return: 是isbn还是key
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
