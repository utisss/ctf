from flask import Flask
from flask import request, redirect, render_template, jsonify
from secrets import *
import MySQLdb

app = Flask(__name__)

def connect():
    db = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)
    return db

def get_data(name):
    db = connect()
    cursor = db.cursor()
    cursor.execute(""" SELECT name, data from data WHERE name = '%s'""" % (name, ))
    data = cursor.fetchall()
    db.close()

    result = [{"name": d[0], "data": d[1],} for d in data]
    """
    if len(result) == 0:
        result = [{"name": "almost there", "data": "try looking at the comments ;)"}]
    """

    return result

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        pass


@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/easy", methods=["GET", "POST"])
def easy():

    if request.method == "GET":
        return render_template("easy.html", data=[], msg=False)
    if request.method == "POST":
        name = request.form.get("name", "")
        name = name.lower()
        data = get_data(name)
        if len(data) == 0:
            return render_template("easy.html", data=data, msg=True)
        return render_template("easy.html", data=data, msg=False)

@app.route("/time", methods=["GET"])
def time():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)
