# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/5 16:14
# 文件   : __init__.py.py
# IDE   : PyCharm
'''dao层初始化所有表，以后新增一个表都需要在这儿import一次'''
from app.models import db
from app.models.user import User

db.create_all()