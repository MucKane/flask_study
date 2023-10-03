from wtforms import Form,StringField
from flask import session
from wtforms.validators import ValidationError,Length

class RegisterForm(Form):
    code = StringField(validators=[Length(4,4)])

    def validate_code(self,field): #自定义验证器 validate_后面紧跟前端的变量名
        font_code = field.data
        server_data = int(session.get('code'))
        print(font_code,server_data)
        if font_code != server_data:
            raise ValidationError('验证码不一致')