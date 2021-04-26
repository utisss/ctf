import subprocess
import os
import re
from random import randrange

from flask import *

# set up upload/extract folders
UPLOAD_DIR = 'uploads'
if not os.path.isdir(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)

# configure app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
app.config['MAX_CONTENT_PATH'] = 2 ** 17 # 128 KB
app.secret_key = 'l1k29348n1goin198ndgn1e'

# creates a secured version of the filename
def secure_filename(filename):
    # strip extension and any sneaky path traversal stuff
    filename, file_ext = os.path.splitext(filename)
    if file_ext is None:
        file_ext = ''
    filename = os.path.basename(filename)
    # add extension
    filename += '__'+hex(randrange(10000000))[2:]+file_ext
    return filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print('uploading file...', flush=True)
    if 'file' not in request.files:
        return redirect('/')
    f = request.files['file']
    if f.filename == '':
        flash('No file selected!')
        return redirect('/')
    filename = secure_filename(f.filename)
    print(filename, flush=True)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Successfully uploaded to "/suggestions/{}"!'.format(filename))
    return redirect('/')

@app.route('/suggestions/<path:path>') 
def send_uploads(path):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], path))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
