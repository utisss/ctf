from flask import *
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "arnold": generate_password_hash("g3t-t0-da-ch0ppa!"),
}

@app.route('/flag', methods=['GET'])
@auth.login_required
def index():
    return render_template('index.html', user=auth.current_user())

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

if __name__ == '__main__':
    app.run(host='0.0.0.0')
