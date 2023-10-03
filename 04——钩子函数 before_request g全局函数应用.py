# 钩子函数可以当作特殊的装饰器
from flask import Flask,g,session

app = Flask(__name__)

from os import urandom
app.secret_key = urandom(24)

@app.route('/')
def hello():
    return 'hello'

@app.route('/login')
def login():
    session['uname']='yj'
    return '账户登陆信息设置成功'

@app.route('/index')
def index():
    if hasattr(g,'uname'):
        return f'{g.uname}登陆成功'
    return '登陆失败'

@app.before_request
def before_request():
    print('每次相应前的应用')
    uname = session.get('uname')
    if uname:
        g.uname = uname


#context_processor 在所有模版中都可以使用


if __name__ == '__main__':
    app.run(debug=True)