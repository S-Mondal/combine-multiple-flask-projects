from flask import Flask, render_template
from project1.app import project1
from project2.app import project2

app = Flask(__name__)
app.register_blueprint(project1)
# app.register_blueprint(project2)

if __name__ == '__main__':
	app.run(port=7000)