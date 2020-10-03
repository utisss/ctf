from flask import *
import pdfkit
import subprocess
import time
import os
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        html = render_template('document.html', content=request.form.get('content'))
        uid = str(hash(time.time()))
        out_filename = uid+'.pdf'
        html_filename = uid+'.html'
        html_file = open(html_filename, 'w')
        html_file.write(html)
        html_file.close()

        subprocess.run(['xvfb-run', 'wkhtmltopdf','--enable-local-file-access', html_filename, out_filename])
        
        out_file = open(out_filename, 'rb')
        output = out_file.read()
        out_file.close()
        #os.remove(out_filename)
        #os.remove(html_filename)

        response = make_response(output)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=document.pdf'
        return response
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

