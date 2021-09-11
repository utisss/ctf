from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template

from sqlalchemy.sql import text
from sqlalchemy import exc

import os

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

@app.route('/', methods=['POST'])
def login():
    email = request.form['email']

    login_sql = "SELECT username FROM users WHERE email='{}'".format(email)

    try:
        result = db.engine.execute(text(login_sql)).fetchall()
        res = [a[0] for a in result]
        return str(res)
    except exc.SQLAlchemyError as e:
        return "error"

if __name__ == '__main__':
    app.run()
