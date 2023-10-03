from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Length,equal_to,Regexp,Email,NumberRange

class RegisterForm(Form):
    uname = StringField(validators=[InputRequired(message='需要输入用户名')])
    pwd = StringField(validators=[Length(min=2,max=10,message='密码长度应为2-10')])
    pwd2 = StringField(validators=[equal_to('pwd',message='两次密码应一致')])
    number = StringField(validators=[Regexp('^1[2-9]\d{9}$')])
    age = IntegerField(validators=[NumberRange(min=18,message='最小年龄应大于18岁')])
    email = StringField(validators=[Email()])
