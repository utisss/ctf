from flask import *
import os

# configure app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('flag', 'utflag{g00d_w0rk_1nsp3ct0r}')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
