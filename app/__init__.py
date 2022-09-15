# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:26
# 文件   : __init__.py
# IDE   : PyCharm
from flask import Flask

from config import Config


pity = Flask(__name__)


pity.config.from_object(Config)