import flask
import requests
import os
from bs4 import BeautifulSoup

app = flask.Flask(__name__)

# ok the actual http code starts here
@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
    url = flask.request.form["url"]
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        soup = soup.get_text().replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
        return flask.render_template("text.html", text=soup)
    else:
        flask.abort(400)

@app.route("/admin")
def admin():
    if flask.request.remote_addr == "127.0.0.1" or flask.request.remote_addr == "::1":
        return os.environ["FLAG"]
    else:
        return flask.render_template("forbidden.html"), 403
