from flask import Flask, request

app = Flask(__name__)
flag = open('flag.txt', 'r').read()

@app.route('/', methods=['GET'])
def index():
    if request.cookies.get("auth", False) == 'SUPERSECRETCOOKIE':
        return flag
    else:
        return 'womp womp'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
