import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.models import User


@inject
@dataclass
class UserService:
    """user服务逻辑逻辑"""
    db: SQLAlchemy

    def create_user(self, email: str, name: str, password: str) -> User:
        """创建用户"""
        # 1. 创建模型类实体
        user = User(name=name, email=email, password=password)
        # 2. 将实体类添加到session中
        self.db.session.add(user)
        # 3. 提交session会话
        self.db.session.commit()
        return user
