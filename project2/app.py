from flask import Flask, render_template
from test import test_api

app = Flask(__name__)
app.register_blueprint(test_api)

@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(port=7000)