from flask import Flask, request, render_template, redirect
import os
app = Flask(__name__)

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import random
important_videos=["https://pbs.twimg.com/profile_images/573997632005140480/e4fLdoY2_400x400.jpeg"]


@app.route("/")
def parseRequest():
    query = request.args.get('query')
    if query is not None and "drop" in query.lower():
        return redirect("https://www.youtube.com/watch?v=22gTAfZmvcM", code=302)

    try:
        connection = pymysql.connect(host='issshacktxctf.ckbsn9tznnjx.us-west-2.rds.amazonaws.com',
                                     user='ctf',
                                     db= "ads",
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        print(query)
        if query is None:
            query = ""
        with connection.cursor() as cursor:
            query = " SELECT * from ads " + query + " limit 3;"
            print(query)
            cursor.execute(query)
            query_result = cursor.fetchall()
            print(query_result)
            connection.close()
    except Exception as e:
        print(e)
        return redirect(random.choice(important_videos), code=302)
    return render_template("index.html", result=query_result)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)
