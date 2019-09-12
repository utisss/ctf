from flask import Flask, render_template, request

app = Flask(__name__)
flag = open('flag.txt', 'r').read()

@app.route('/', methods=['GET', 'POST'])
def index():
    temp = 250
    if request.method == 'GET':
        return render_template('index.html', temp=temp)
    else:
        temp = int(request.form['temp'])
        if temp <= 400 and temp >= 100:
            resp = f'Temperature set to {temp}°F'
        else:
            emoji = "🔥🔥" if temp > 400 else "❄️❄️"
            resp = emoji + flag + emoji
        return render_template('index.html', resp=resp, temp=temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
