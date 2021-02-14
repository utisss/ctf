from flask import Flask,render_template, send_from_directory,request,redirect
from os import listdir
from os.path import isfile, join
import subprocess

app = Flask(__name__)


def is_png(f):
    return f.split(".")[1] == "png"

@app.route('/')
def uwu():
    return render_template("index.html")

@app.route('/stonks/<path:path>')
def stonks(path):
    if "-R" in path:
        return "3lon doesn't like -R sorry"
    if "|" in path:
        return "no pipes, 3lon is more of a tunnel guy"
    return "stocks are up by " + subprocess.check_output(path.split(" ")).decode("utf-8") + " points",200

@app.route('/imgs/<path:path>')
def get_img(path):
    return send_from_directory("./imgs/",path)

@app.route('/main.py')
def Pog():
    return send_from_directory('.','main.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
