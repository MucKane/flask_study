from flask import Flask,render_template,request
from wtforms import StringField,Form   
from wtforms.validators import Length,EqualTo

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

class RegisterForm(Form):
    uname = StringField(validators=[Length(min=2,max=5,message='用户名长度需要在2-5')])
    pwd = StringField(validators=[Length(min=2,max=5,message='密码长度应位于2-5')])
    pwd2 = StringField(validators=[EqualTo('pwd',"两次密码不一致")])

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            return '验证成功'
        else:
            return f'验证失败{form.errors}'
        
if __name__ == '__main__':
    app.run(debug=True)