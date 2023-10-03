from flask import Flask,abort

app = Flask(__name__)

@app.errorhandler(404) #处理错误的状态
def error_404(error):
    return '404 not found --error',404

@app.errorhandler(500)
def error_500(error):
    return '500 --error',500

@app.route('/')
def hello():
    return 'hello'

@app.route('/home')
def error_test():
    abort(500)
if __name__ == '__main__':
    app.run()

