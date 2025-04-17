from datetime import datetime
import uuid
from sqlalchemy import PrimaryKeyConstraint, Column, UUID, String, Text, DateTime, Index

from internal.extension.database_extension import db


class User(db.Model):
    """用户模型类"""
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_user_id'),
        Index('idx_user_email', 'email'),
    )

    id = Column(UUID, default=uuid.uuid4(), primary_key=True, nullable=False)
    email = Column(String(200), nullable=False)
    name = Column(String(200), default="", nullable=False)
    password = Column(String(200), nullable=False)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
