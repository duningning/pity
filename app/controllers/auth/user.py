# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 16:19
# 文件   : user.py.py
# IDE   : PyCharm
from app.middleware.Jwt import UserToken
from app.handler.factory import ResponseFactory

from flask import Blueprint
from flask import jsonify

from flask import request
from app.dao.auth.UserDao import UserDao

auth = Blueprint("auth", __name__, url_prefix="/auth")


# 这里以auth.route注册的函数都会自带/auth，所以url是/auth/register
@auth.route("/register", methods =['POST'])
def register():  #code=101是参数错误，110是异常错误, 0是正常返回
    #获取request请求数据
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=101,msg="用户名或密码不能为空"))
    email, name =data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(code=101,msg="姓名和邮箱不能为空"))
    err = UserDao.register_user(username, name, password, email)
    if err is not None:
        return jsonify(dict(code=110,msg=err))
    return jsonify(dict(status=True, msg="注册成功"))

@auth.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=101, msg="用户名或密码不能为空"))
    user, err = UserDao.login(username, password)
    if err is not None:
        return jsonify(dict(code=110, msg=err))

    user = ResponseFactory.model_to_dict(user, "password")
    token = UserToken.get_token(user)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg="登录成功", data=dict(token=token, user=user)))