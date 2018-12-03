from flask import Flask, request, render_template, redirect, send_file
import os
app = Flask(__name__)

#wyd messing around in the source code man, why aren't you chugjugging the fortnite???

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/page")
def parseRequest():
    try:
        path = os.path.join("templates", request.args.get("page"))
        print(path)
        if "html" in str(request.args.get("page")):
            return send_file(path, mimetype='text/html')
        return send_file(path)
    except Exception as e:
        print(e)
        return render_template("404.html")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
