from flask import *
from flask_socketio import SocketIO, send, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a85nq0gon12.g0aslk50'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('get_flag')
def handle_message(data):
    send('utflag{w3bs0ck3t5_r0ck!}')
    disconnect()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
