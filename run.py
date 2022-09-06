# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:27
# 文件   : run.py.py
# IDE   : PyCharm
from datetime import datetime

from app import pity
from app.utils import Log
from app import dao

@pity.route('/')
def hello_world():
    log = Log('Hello world专用')
    log.info('有人访问你的网站了')
    return 'Hello World!'


if __name__ == "__main__":
    pity.run("0.0.0.0", threaded=True, port="7777")
