from flask import *
import jwt
app = Flask(__name__)
KEY = None
FLAG = "utflag{IM_DAVID_S_PUMPKINS_MAN}"

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))

    if not 'token' in request.cookies:
        payload = {
            "is_admin": False
        }
        resp.set_cookie('token', jwt.encode(payload, KEY, algorithm="none"))
    else:
        token = request.cookies.get('token')
        try:
            payload = jwt.decode(token, verify=False)
        except:
            return "could not decode token"
        if payload["is_admin"]:
            return FLAG
    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
