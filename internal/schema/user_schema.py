from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length


class LoginRequest(FlaskForm):
    """登陆请求验证"""
    email = EmailField('email', validators=[DataRequired(message="邮箱必填")])
    password = PasswordField('password', validators=[DataRequired(), Length(max=50, message="最大50个字")])


class RegisterRequest(FlaskForm):
    """登陆请求验证"""
    email = EmailField('email', validators=[DataRequired(message="邮箱必填")])
    name = StringField('name', validators=[DataRequired(), Length(max=50, message="最大50个字")])
    password = PasswordField('password', validators=[DataRequired(), Length(max=50, message="最大50个字")])
