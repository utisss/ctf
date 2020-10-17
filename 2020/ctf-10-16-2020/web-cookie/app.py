from flask import *
app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def index():
    resp = make_response(render_template('index.html'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'real-fan' and password == 'elon-musk-is-my-god':
            resp = make_response(redirect('/flag', code=302))
            resp.set_cookie('user', 'guest')
    return resp

@app.route('/flag')
def flag():
    cookie = request.cookies.get('user')
    if not cookie is None:
        if cookie == 'guest':
            return render_template('guest.html')
        elif cookie == 'elon':
            return render_template('elon.html')
    return redirect('/login', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
