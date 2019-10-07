from contextlib import contextmanager


class MyTest:
    def speak(self):
        print('说话')


@contextmanager
def my_test():
    print('在开始之前')
    yield MyTest()
    print('在开始之后')


with my_test():
    print('中间')
