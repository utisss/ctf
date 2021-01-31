from flask import *
from flask_socketio import SocketIO, send, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = '1089an1123ongoj'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('get_flag')
def handle_message(data):
    if data['passwd'] == 'beep-boop':
        send('utflag{l33t_w3b50ck3t5_hack}')
    else:
        send('Wrong password!')
    disconnect()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
