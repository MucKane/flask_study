from flask import Flask,render_template,views,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

from os import urandom
app.secret_key=urandom(24)

class LoginView(views.MethodView):
    def __jump(self,msg=None):
        return render_template('login.html',msg=msg)
    def get(self):
        msg = request.args.get('msg')
        return self.__jump(msg=msg)
    def post(self):
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        if uname == 'yj' and pwd == '123':
            session['uname'] = uname
            return render_template('index.html')
        else:
            return self.__jump(msg='用户名或密码错误')

app.add_url_rule('/login',view_func=LoginView.as_view('login'))

@app.route('/index')
def index():
    uname = session.get('uname')
    if uname:
        return render_template('index.html')
    return redirect(url_for('login',msg='请先登陆'))

if __name__ == '__main__':
    app.run(debug=True)