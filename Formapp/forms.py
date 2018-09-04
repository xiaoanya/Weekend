from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    proname = StringField(label="名称",validators=[DataRequired()])
    submit = SubmitField(label="点击提交")
class LoginForm(FlaskForm):
    username = StringField(label="用户名",validators=[DataRequired()])
    password = PasswordField(label="密码",validators=[DataRequired()])
    submit = SubmitField(label="登录")