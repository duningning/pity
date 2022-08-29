# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 15:11
# 文件   : decorator.py
# IDE   : PyCharm
'''
    这是一个装饰器方法文件
'''


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.cls(*args, **kwds)
        return self.instance
