# -*-coding:utf-8-*-
# 作者:duningning.ming
# 创建时间: 2022/8/29 14:27
# 文件   : run.py.py
# IDE   : PyCharm
from datetime import datetime

from app import pity
from app.utils.logger import Log
from app.controllers.auth.user import auth

from app import dao #使得建表语句db.create_all()生效
#注册蓝图
pity.register_blueprint(auth)


@pity.route('/')
def hello_world():
    log = Log('Hello world专用')
    log.info('有人访问你的网站了')
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    print(now)
    return now


if __name__ == "__main__":
    pity.run("0.0.0.0", threaded=True, port="7777")
