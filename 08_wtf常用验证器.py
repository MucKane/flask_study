from flask import Flask,request,render_template
from flask.views import MethodView
from check.formcheck import RegisterForm
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

class wtf(MethodView):
    def __jump(self):
        return render_template('wtf.html')
    def get(self):
        return self.__jump()
    def post(self):
        form = RegisterForm(request.form)#获取表单数据
        if form.validate():
            return '验证成功'
        else:

            return f'验证失败{form.errors}'

app.add_url_rule('/wtf',view_func=wtf.as_view('wtf_test'))
if __name__ == '__main__':
    app.run(debug=True,port=5050)