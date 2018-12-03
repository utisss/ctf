from flask import Flask, request, render_template, redirect, send_file, make_response
import os
app = Flask(__name__)


@app.route("/")
def render_home():
    if request.cookies.get('sess') is None:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('sess', "eyJ1c2VyIjowRkE2MUNFNDYzNUVDRkYyQUJDRUQ1NTdENjlFMjYxOTRDNzA2NzQzIn0")
        return resp
    if request.cookies.get('sess') != 'eyJ1c2VyIjowRkE2MUNFNDYzNUVDRkYyQUJDRUQ1NTdENjlFMjYxOTRDNzA2NzQzIn0' and request.cookies.get('sess') != "eyJ1c2VyIjpEMDMzRTIyQUUzNDhBRUI1NjYwRkMyMTQwQUVDMzU4NTBDNERBOTk3In0":
        return render_template('cookie_edit.html')
    elif request.cookies.get('sess') == "eyJ1c2VyIjpEMDMzRTIyQUUzNDhBRUI1NjYwRkMyMTQwQUVDMzU4NTBDNERBOTk3In0":
        return render_template('victory.html')
    else:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('sess', "eyJ1c2VyIjowRkE2MUNFNDYzNUVDRkYyQUJDRUQ1NTdENjlFMjYxOTRDNzA2NzQzIn0")
        return resp




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
