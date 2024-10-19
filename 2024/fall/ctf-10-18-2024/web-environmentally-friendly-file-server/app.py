from flask import *
app = Flask(__name__)

@app.route('/', defaults=dict(filename=None))
@app.route('/<path:filename>', methods=['GET'])
def index(filename):
    filename = filename or 'index.html'
    filename = './files/' + filename
    with open(filename, 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
