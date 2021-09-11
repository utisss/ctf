import flask
import sqlite3
import os
import pickle, hmac, base64

secret = base64.b64decode(os.environ["SECRET"].encode("ascii"))
ddir = os.environ["DATA_DIR"]
sq_file = ddir + "/users.db"
notes_dir = ddir + "/notes/"
# initialization stuff
if not os.path.isfile(sq_file):
    with sqlite3.connect(sq_file) as sq:
        sq = sqlite3.connect(sq_file)
        cur = sq.cursor()
        cur.execute("CREATE TABLE users (username text, password text)")
        cur.execute("INSERT INTO users VALUES ('bankerman', ?)", (os.environ["ADMIN_PASSWD"],))
        sq.commit()

if not os.path.isdir(notes_dir):
    os.mkdir(notes_dir)
if not os.path.isfile(notes_dir + "bankerman"):
    with open(notes_dir + "bankerman", "w") as adminnotes:
        adminnotes.write("""
TODO:
 - process payments for that guy who owns all the railroads
 - go to jail to exchange ones for hundreds
 - yell at security people about password change policy

New username: BankerMan06
Password: {}
                """.format(os.environ["FLAG"]))

def check_characters(string):
    bad = "/\x00"
    for c in string:
        if c in bad:
            return False
    return True

def un_cookie(un):
    d = {
            "s": hmac.digest(secret, un.encode("utf-8"), "sha256"),
            "u": un
            }
    p = pickle.dumps(d)
    return base64.b64encode(p).decode("ascii")

class InvalidCookieException(Exception):
    pass

def cookie_un(cookie):
    p = base64.b64decode(cookie)
    d = pickle.loads(p)
    h = hmac.digest(secret, d["u"].encode("utf-8"), "sha256")
    if d["s"] == h:
        return d["u"]
    else:
        raise InvalidCookieException

app = flask.Flask(__name__)

# ok the actual http code starts here
@app.route("/")
def index():
    sess = flask.request.cookies.get("notes-session")
    if sess:
        return flask.redirect(flask.url_for("notepad"))
    else:
        return flask.render_template("index.html")

@app.route("/notepad", methods=["GET"])
def notepad():
    sess = flask.request.cookies.get("notes-session")
    if sess:
        try:
            username = cookie_un(sess)
            with open(notes_dir + username, "r") as notesfile:
                return flask.render_template("notepad.html", notes=notesfile.read())
        except InvalidCookieException:
            resp = flask.make_response(flask.redirect(flask.url_for("login_page")))
            resp.set_cookie("notes-session", "", expires=0)
            return resp
    else:
        return flask.redirect(flask.url_for("login_page"))

@app.route("/notepad", methods=["POST"])
def notepad_save():
    sess = flask.request.cookies.get("notes-session")
    if sess:
        try:
            username = cookie_un(sess)
            with open(notes_dir + username, "w") as notesfile:
                notesfile.write(flask.request.form["notes"])
            return flask.redirect(flask.url_for("notepad"))
        except InvalidCookieException:
            resp = flask.make_response(flask.redirect(flask.url_for("login_page")))
            resp.set_cookie("notes-session", "", expires=0)
    else:
        return flask.redirect(flask.url_for("login_page"))

@app.route("/login", methods=["GET"])
def login_page():
    return flask.render_template("logreg.html", desc="Login")

@app.route("/register", methods=["GET"])
def register_page():
    return flask.render_template("logreg.html", desc="Register")

@app.route("/register", methods=["POST"])
def register():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if not check_characters(username):
        flask.abort(401)
    with sqlite3.connect(sq_file) as sq:
        cur = sq.cursor()
        cur.execute("SELECT username FROM users WHERE username=?", (username,))
        if cur.fetchone():
            return flask.render_template("logreg.html", desc="Register", error="User already exists")
        cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        sq.commit()
    open(notes_dir + username, "a").close()
    return flask.redirect(flask.url_for("login_page"))

@app.route("/login", methods=["POST"])
def login():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    with sqlite3.connect(sq_file) as sq:
        cur = sq.cursor()
        cur.execute("SELECT username FROM users WHERE username=? AND password=?", (username, password))
        if cur.fetchone():
            resp = flask.make_response(flask.redirect(flask.url_for("notepad")))
            resp.set_cookie("notes-session", un_cookie(username))
            return resp
        else:
            return flask.render_template("logreg.html", desc="Login", error="Incorrect password")
