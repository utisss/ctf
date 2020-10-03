from flask import *
import urllib
app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'red-imposter' and password == 'imposters-ALWAYS-win':
            return render_template('flag.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

