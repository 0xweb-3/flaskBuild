import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from internal.models import User
from internal.router import Router
from pkg.exception.exception import CustomException
from pkg.response.http_code import HttpCode
from pkg.response.response import json, Response


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 通过类的方式将应用配置加载
        self.config.from_object(conf)
        # 注册应用路由
        router.register_router(self)

        # 初始化SQLAlchemy扩展
        db.init_app(self)

        # 创建数据库表
        with self.app_context():
            _ = User()  # 确保项目代码一定能检索到app模型
            db.create_all()

        # 绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

    def _register_error_handler(self, err: Exception):
        # 1.异常信息是不是我们的自定义异常，如果是可以提取message和code等信息
        if isinstance(err, CustomException):
            return json(Response(
                code=err.code,
                message=err.message,
                data=err.data if err.data is not None else {}
            ))

        # 2.如果不是我们的自定义异常，则有可能是程序
        if self.debug or os.getenv('FLASK_ENV') == "development":
            raise err
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(err),
                data={}
            ))
