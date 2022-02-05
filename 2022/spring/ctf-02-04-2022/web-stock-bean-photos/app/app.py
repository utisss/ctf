from flask import *
import os

# configure app
app = Flask(__name__)
print(os.listdir('.'))

options = os.listdir('images')

@app.route('/download', methods=['POST'])
def process_vote():
    fname = request.form.get('filename')
    if not fname:
        abort(404)
    path = os.path.abspath('images/'+fname)
    return send_file(path)

@app.route('/', methods=['GET'])
def index(favVeg=None):
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
