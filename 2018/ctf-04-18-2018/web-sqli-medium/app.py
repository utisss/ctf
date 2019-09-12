from flask import Flask
from flask import request, redirect, render_template, jsonify
from secrets import *
import MySQLdb

app = Flask(__name__)

def connect():
    db = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)
    return db

def get_reviews(rating):
    db = connect()
    cursor = db.cursor()
    print(""" SELECT name, review, rating from reviews WHERE rating = '%s'""" % (rating, ))
    cursor.execute(""" SELECT name, review, rating from reviews WHERE rating = '%s'""" % (rating, ))
    data = cursor.fetchall()
    db.close()

    result = [{"name": d[0], "review": d[1], "rating": d[2],} for d in data]

    return result


@app.route("/", methods=["GET", "POST"])
def med():

    if request.method == "GET":
        return render_template("med.html", data=[])
    if request.method == "POST":
        rating = request.form.get("rating", 0)
        data = get_reviews(rating)
        return render_template("med.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
