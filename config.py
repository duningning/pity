# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:47
# 文件   : config.py
# IDE   : PyCharm
#基础配置类
import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log')