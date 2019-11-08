from flask import Flask

app = Flask(__name__)
flag = open('flag.txt', 'r').read()

@app.route('/', methods=['GET'])
def index():
    return flag

if __name__ == '__main__':
    app.run(host='0.0.0.0')
