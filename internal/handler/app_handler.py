from flask import request

from internal.schema.user_schema import LoginRequest


class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"data": "pong"}

    def login(self):
        req = LoginRequest()
        if not req.validate():
            return {"data": req.errors}
        return {"data": request.json.get("email")}
