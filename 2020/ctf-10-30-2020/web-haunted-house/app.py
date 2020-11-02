from flask import *
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
@app.route('/login', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        spooky = request.form.get('spooky')
        if spooky == 'true':
            return redirect('/behind-the-bookcase?name='+name, code=302)
        else:
            return redirect('/fail?name='+name, code=302)
    return render_template('index.html')

@app.route('/fail')
def fail():
    name = request.args.get('name')
    return render_template('fail.html', name=name)

@app.route('/behind-the-bookcase')
def flag():
    name = request.args.get('name')
    return render_template('flag.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
