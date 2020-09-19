from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "pog utflag{welc0me_t0_th3_d4rk_w3b}"

app.run(host="0.0.0.0", port=8080)

