from flask import *
import urllib
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url is None:
            try:
                res = urllib.request.urlopen(url)
                content = res.read()
                if len(content) > 512:
                    content = content[:512].decode('utf8')+' ...'
            except:
                content = 'That URL was invalid!'
            return render_template('index.html', content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
