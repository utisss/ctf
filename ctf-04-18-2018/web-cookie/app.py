import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='website/build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
	if(path == ""):
		return send_from_directory('website/build', 'index.html')
	else:
		if(os.path.exists("website/build/" + path)):
			return send_from_directory('website/build', path)
		else:
			return send_from_directory('website/build', 'index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', use_reloader=True, port=5000, threaded=True)
