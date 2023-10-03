from flask import Flask,render_template,request,send_from_directory
# 处理包含文件路径名等的情况
from werkzeug.utils import secure_filename
import os

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'imgs')

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        file = request.files.get('file')
        file_name = file.filename
        filename = secure_filename(file_name)
        #保存文件
        file.save(os.path.join(UPLOAD_PATH,filename))
        return filename


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_PATH,filename)


if __name__ == '__main__':
    app.run(debug=True)