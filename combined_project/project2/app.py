from flask import Blueprint, render_template
from project2.test import test_api

project2 = Blueprint('project2',__name__, url_prefix='/project2')
project2.register_blueprint(test_api)

@project2.route('/')
def index():
	return render_template("project2/index.html")
