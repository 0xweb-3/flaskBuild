import uuid

from flask import request

from internal.models import User
from internal.schema.user_schema import LoginRequest, RegisterRequest
from internal.service.user_service import UserService
from pkg.exception.exception import NotFoundException
from pkg.response.response import validate_error_json, success_json


class UserHandler:
    """应用控制器"""
    user_service: UserService

    def ping(self):
        return {"data": "pong"}

    def login(self):
        req = LoginRequest()
        if not req.validate():
            return validate_error_json(req.errors)
        return success_json({"data": request.json.get("email")})

    def register(self):
        req = RegisterRequest()
        if not req.validate():
            return validate_error_json(req.errors)
        user = self.user_service.create_user(req.email, req.name, req.password)
        return success_json({"user_id": user.id})
