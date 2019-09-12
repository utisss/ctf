from flask import Flask, request, render_template, redirect
import os
app = Flask(__name__)

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import random
important_videos=["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=EoidKFUVkhM", "https://www.youtube.com/watch?v=cwQgjq0mCdE", "https://www.cs.utexas.edu/~asper/", "https://www.youtube.com/watch?v=MVwv26Q1pVU", "https://www.youtube.com/watch?v=22gTAfZmvcM", "https://www.youtube.com/watch?v=-omR1rXcPrE"]


@app.route("/")
def parseRequest():
    query = request.args.get('query')
    print(query)
    if query is None:
        return render_template("index.html")
    if "drop" in query.lower():
        return redirect("https://www.youtube.com/watch?v=22gTAfZmvcM", code=302)

    try:
        connection = pymysql.connect(host='isssctf.ckbsn9tznnjx.us-west-2.rds.amazonaws.com',
                                     user='ricks',
                                     password="",
                                     db= "EarthC137",
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            query = " SELECT name, description from ricks WHERE name = \'" + query + "\';"
            print(query)
            cursor.execute(query)
            query_result = cursor.fetchall()
            print(query_result)
    except Exception as e:
        print(e)
        connection.close()
        return redirect(random.choice(important_videos), code=302)
    connection.close()
    return render_template("result.html", result=query_result)

@app.route("/200IQONLY")
def solution():
    return "utflag{the_council_of_ricks_demands_your_presence}"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
