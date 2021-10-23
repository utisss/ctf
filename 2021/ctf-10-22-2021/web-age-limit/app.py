from flask import *

# configure app
app = Flask(__name__)

@app.route('/age', methods=['POST'])
def process_vote():
    age = int(request.form.get('age'))
    msg = 'Age entered successfully.'
    if age >= 18:
        msg += ' Looks like you''re old enough! utflag{weird_webapp_mature_social_experiment}'
    return redirect(url_for('index', msg=msg))

@app.route('/', methods=['GET'])
def index():
    msg = request.args.get('msg')
    if msg:
        return render_template('index.html', message=msg)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
