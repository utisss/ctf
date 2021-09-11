from flask import *
import urllib
app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'thimble' and password == 's3cr3t-p@ssw0rd!':
            if request.environ['REMOTE_ADDR'] == '127.0.0.1':
                resp = make_response(redirect('/flag', code=302))
                resp.set_cookie('Authorization', '6db74f1d24c70f46')
                return resp
            else:
                return render_template('ip-denied.html')
    return render_template('index.html')

@app.route('/flag')
def flag():
    cookie = request.cookies.get('Authorization')
    if not cookie is None and cookie == '6db74f1d24c70f46':
        return render_template('flag.html')
    return render_template('access-denied.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

