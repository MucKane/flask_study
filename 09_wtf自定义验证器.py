from flask import Flask,render_template,session,request
from flask.views import MethodView
from random import randint
from check.createdform import RegisterForm

app = Flask(__name__)
from os import urandom
app.secret_key=urandom(24)

@app.route('/')
def home():
    return 'hello'

class Wtf(MethodView):
    def __jump(self,code=None):
        return render_template('code.html',code=code)
    def get(self):
        code = randint(1000,9999)
        session['code'] = code
        return self.__jump(code)
    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            return '验证成功'
        else:
            return f"验证失败,{form.errors}"

app.add_url_rule('/wtf',view_func=Wtf.as_view('test'))

if __name__ == '__main__':
    app.run(debug=True)