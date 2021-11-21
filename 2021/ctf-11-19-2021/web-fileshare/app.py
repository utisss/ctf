import flask
import os
import pathlib
import re

ddir = os.environ["DATA_DIR"]
namere = re.compile(r'^(\d+)-')

app = flask.Flask(__name__)

# ok the actual http code starts here
@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/api/file/<int:id>")
def notepad(id):
    search = str(id) + "-"
    response = {}
    for ent in pathlib.Path(ddir).rglob("*-*"):
        if ent.name.startswith(search) and not ent.is_dir():
            response["id"] = id
            response["filename"] = ent.name.removeprefix(search)
            m = namere.match(ent.parent.name)
            if m:
                response["parent"] = int(m.group(1))
            response["download"] = flask.url_for('download', id=id)
            response["modified"] = ent.stat().st_mtime
            return response
    flask.abort(404)

@app.route("/api/download/<int:id>")
def download(id):
    search = str(id) + "-"
    for ent in pathlib.Path(ddir).rglob("*-*"):
        if ent.name.startswith(search) and not ent.is_dir():
            with open(ent, 'r') as f:
                return f.read()
    flask.abort(404)

@app.route("/api/dir/<int:id>")
def directory(id):
    search = str(id) + "-"
    response = {}
    for ent in pathlib.Path(ddir).rglob("*-*"):
        if ent.name.startswith(search) and ent.is_dir():
            response["id"] = id
            response["filename"] = ent.name.removeprefix(search)
            m = namere.match(ent.parent.name)
            if m:
                response["parent"] = int(m.group(1))
            response["entries"] = []
            for child in ent.iterdir():
                r2 = {}
                m2 = namere.match(child.name)
                if m2:
                    r2["id"] = int(m2.group(1))
                    r2["dir"] = child.is_dir()
                    response["entries"].append(r2)
            return response
