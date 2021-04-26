from flask import *

# configure app
app = Flask(__name__)

VOTES = [0, 0, 100000, 0]

@app.route('/vote', methods=['POST'])
def process_vote():
    req_votes = [int(request.form.get('flag1')),
                 int(request.form.get('flag2')),
                 int(request.form.get('flag3')),
                 int(request.form.get('flag4'))]
    prev_win = VOTES.index(max(VOTES))
    for i in range(4):
        VOTES[i] += req_votes[i]
    new_win = VOTES.index(max(VOTES))

    msg = 'Succesfully cast your vote!'
    if prev_win != new_win:
        msg += ' Wow, that was unexpected. utflag{never_trust_dirty_client_side_sanitization}'
    return redirect(url_for('index', msg=msg))

@app.route('/', methods=['GET'])
def index():
    msg = request.args.get('msg')
    if msg:
        return render_template('index.html', votes=VOTES, message=msg)
    else:
        return render_template('index.html', votes=VOTES)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
