# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/9/6 10:18
# 文件   : Jwt.py.py
# IDE   : PyCharm
import hashlib
from datetime import timedelta, datetime

import jwt
from jwt.exceptions import ExpiredSignatureError

EXPIRED_HOUR = 3


class UserToken(object):
    key = 'pityToken'
    salt = 'pity'

    @staticmethod
    def get_token(data):
        new_data = dict({"exp": datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)}, **data)
        return jwt.encode(new_data, key=UserToken.key).decode()

    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception("token已过期, 请重新登录")

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        m.update(password + UserToken.salt)
        return m.hexdigest()