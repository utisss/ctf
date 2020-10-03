from flask import Flask,render_template, send_from_directory,request,redirect
from os import listdir
from os.path import isfile, join
import subprocess

app = Flask(__name__)


flag = open("flag.txt")

def is_png(f):
    return f.split(".")[1] == "png"

@app.route('/')
def uwu():
    imgs = [f for f in listdir("imgs/") if isfile(join("imgs/",f)) and is_png(f)][0:5]
    print(imgs)
    return render_template("index.html",imgs=imgs)

@app.route('/upload', methods=['POST'])
def upload_UWO():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '' and is_png(uploaded_file.filename):
        uploaded_file.save("./imgs/" +uploaded_file.filename)
    return redirect("/")

@app.route('/img/<path:path>')
def OwO(path):
    return send_from_directory('./imgs/',path)


@app.route('/exec/<path:path>')
def executescript(path):
    return subprocess.check_output(['python',path])

@app.route('/main.py')
def Pog():
    return send_from_directory('.','main.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
