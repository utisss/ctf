from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/msg", methods=['GET'])
def key():
    print('in post')
    print(request.args)
    key = request.args.get("key", "")
    print(key)
    
    if key == "cmeTeLFe8Ak4OB5p":
        return "utflag{b4ck_t0_th3_Futur3}"

    return "close, but no cigar"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
