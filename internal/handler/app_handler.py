from flask import request

from internal.schema.user_schema import LoginRequest
from pkg.exception.exception import NotFoundException
from pkg.response.response import validate_error_json, success_json


class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"data": "pong"}

    def login(self):
        # 1/0
        raise NotFoundException()
        req = LoginRequest()
        if not req.validate():
            return validate_error_json(req.errors)
        return success_json({"data": request.json.get("email")})
