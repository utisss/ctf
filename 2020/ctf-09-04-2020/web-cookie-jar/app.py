from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    cookie = request.cookies.get('isCookieMonster')
    resp = make_response(render_template('index.html'))
    if cookie is None:
        resp.set_cookie('isCookieMonster', 'false')
    elif cookie == 'true':
        return render_template('flag.html')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
