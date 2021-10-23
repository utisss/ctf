from flask import *
app = Flask(__name__)

import subprocess
import re

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        url = re.sub('\s+', '', url)
        print(url)
        if not url is None:
            try:
                cmd = 'ping -t 1 -c 1 '
                cmd += url
                process = subprocess.run(cmd, shell=True, capture_output=True)
                if process.returncode == 2:
                    content = '"{}" seems to be down!'.format(url)
                elif process.returncode != 0:
                    content = process.stderr.decode('utf8')
                else:
                    content = '"{}" seems to be up!'.format(url)
            except:
                content = 'That URL was invalid!'
            return render_template('index.html', content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
