from flask import *
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'please don\'t guess this key lmao'

FLAG = "utflag{wow_ur_so_g00d_at_math}"

def gen_challenge():
    return [random.randint(0, 1000), random.randint(0, 1000)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'count' not in session:
        session['count'] = 0
        session['challenge'] = gen_challenge()
    
    soln = request.form.get("solution")
    if not (soln is None) and (soln.isnumeric()):
        soln = int(soln)
        if soln == session['challenge'][0] + session['challenge'][1]:
            session['count'] += 1
            if session['count'] == 500:
                return FLAG
        else:
            session['count'] = 0
        
        session['challenge'] = gen_challenge()

    resp = make_response(render_template('index.html', count=session['count'], challenge=session['challenge']))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
