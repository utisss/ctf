from flask import *
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    return resp

@app.route('/login', methods=['post'])
def login():
    password = request.form.get('password')

    con = sqlite3.connect(':memory:')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE secret_tbl (flag_oops_22)
    ''')

    cur.execute('''
        INSERT INTO secret_tbl VALUES ('utflag{bsqli_k1nda_busted_ajd333}')
    ''')

    con.commit()

    data = cur.execute("SELECT * FROM secret_tbl WHERE flag_oops_22 = '%s'" % password).fetchall()
    
    return "you got the flag!" if len(data) != 0 else "fail"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
