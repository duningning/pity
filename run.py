# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:27
# 文件   : run.py.py
# IDE   : PyCharm
from app import pity


@pity.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    pity.run("0.0.0.0", threaded=True, port="7777")
