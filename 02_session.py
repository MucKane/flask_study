from flask import Response, session, Flask

app = Flask(__name__)

# set secret_key for session
from os import urandom

app.secret_key = urandom(24)  # leaving this will create bug


# set cookies
@app.route("/set_cookie")
def set_cookies():
    resp = Response('set cookie')
    resp.set_cookie('user_age', '18')
    return resp


@app.route('/set_session')
def set_session():
    session['user_name'] = 'yj'  # main content of session, add or modify
    return 'set session'


@app.route('/get_session')
def get_session():
    uname = session.get('user_name')
    return f'data from session is {uname}'


@app.route('/del_session')
def del_session():
    # pop('key')
    session.pop('user_name')
    # clear delete all key
    return 'delete a session'


if __name__ == '__main__':
    app.run(debug=True, port=5050)
