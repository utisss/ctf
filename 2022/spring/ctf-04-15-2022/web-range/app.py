import os
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    return resp

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == '57295738':
        return os.getenv('FLAG')
    return "Wrong password"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
