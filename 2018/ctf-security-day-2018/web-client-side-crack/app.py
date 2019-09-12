from flask import Flask
from flask import request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    _pass = request.form.get("pass", "")
    print(_pass)
    
    if _pass == "sss":
        return render_template("flag.html") 

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, threaded=True)
