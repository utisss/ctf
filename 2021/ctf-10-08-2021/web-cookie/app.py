from flask import *
app = Flask(__name__)

cookie_name = 'isFlagFolk'

@app.route('/')
def index():
    cookie = request.cookies.get(cookie_name)
    if not cookie is None and cookie == 'true':
        return redirect('/flag')
    return render_template('index.html')

@app.route('/flag')
def flag():
    cookie = request.cookies.get(cookie_name)
    if not cookie is None and cookie == 'true':
        return render_template('flag.html')
    return redirect('/')

@app.route('/fail')
def fail():
    return render_template('fail.html')

@app.route('/submit', methods=['POST'])
def submit():
    cookie = request.cookies.get(cookie_name)
    if cookie is None or cookie != 'true':
        resp = make_response(redirect('/fail'))
        resp.set_cookie(cookie_name, 'false')
        return resp
    return redirect('/flag')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
