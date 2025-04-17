from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import UserHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: UserHandler

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建蓝图
        bp = Blueprint('demo', __name__, url_prefix='/v1')
        # 2. 将url与对应的控制器方法绑定
        bp.add_url_rule("/ping", methods=["GET", "POST"], view_func=self.app_handler.ping)
        bp.add_url_rule("/login", methods=["POST"], view_func=self.app_handler.login)

        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
