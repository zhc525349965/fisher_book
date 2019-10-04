# -*- coding: UTF-8 -*-

# Description: $Description$
#      Author: Mario
#    Datetime: 2019-09-28 21:10
import threading
import time

from werkzeug.local import Local


class A(Local):
    def __init__(self):
        super().__init__()


my_obj = A()
my_obj.test_data = 1


def my_func():
    my_obj.test_data = 2
    print(my_obj.test_data)


new_t = threading.Thread(target=my_func)
new_t.start()

time.sleep(2)

print(my_obj.test_data)
