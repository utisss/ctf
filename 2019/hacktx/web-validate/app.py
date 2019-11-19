from flask import Flask, render_template, request

app = Flask(__name__)
flag = open('flag.txt', 'r').read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return render_template('thankyou.html', flag=flag)

if __name__ == '__main__':
    app.run(host='127.0.0.1')
