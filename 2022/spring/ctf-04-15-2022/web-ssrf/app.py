from flask import *
import urllib
import http
import sys

# configure app
app = Flask(__name__)

@app.route('/flag', methods=['GET']) 
def flag():
    if request.remote_addr == '127.0.0.1':
        return 'utflag{ssrf_15_my_fav0r1t3_vu1n}'.encode('utf8')
    return 'Access denied: external IP "{}" is not authorized to view this resource.'.format(request.remote_addr)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url is None:
            try:
                res = urllib.request.urlopen(url)
                if not isinstance(res, http.client.HTTPResponse):
                    raise Exception
                content = res.read()
                if len(content) > 512:
                    content = content[:512].decode('utf8')+' ...'
            except Exception as e:
                print(e)
                content = 'That URL was invalid!'
            return render_template('index.html', content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9436)
