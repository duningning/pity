# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:47
# 文件   : config.py
# IDE   : PyCharm
#基础配置类
import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__)) # 根目录配置
    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log') # log文件路径
    # Flask jsonify编码问题
    JSON_AS_ASCII = False

    #MYSQL连接信息
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = 'Ming6932058_'
    DBNAME = 'pity'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False